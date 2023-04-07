# Flask application to query db
import os, sys
import pika
import json

from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from servicehelper import serviceIsReady, isServiceReady
from time import sleep

'''
AMQP Setup required for sending volunteer data, not operational yet until AMQP is fully configured
#import #{amqp_setup}
'''

app = Flask(__name__)
CORS(app)

PORT = os.environ.get("SIGNUPVOLUNTEER_HOST_PORT")
USER_HOST_PORT = os.environ.get("USER_HOST_PORT")
VOLUNTEEREVENT_HOST_PORT = os.environ.get("VOLUNTEEREVENT_HOST_PORT")

################################################ MOVED TO APIGATEWAY ######################################################
# Get all volunteer event data
# (For UI)
# [GET] /volunteer/event
# Return all volunteer event data from calling volunteer event microservice volunteer.py with invokes.py to parse json data
################################################ MOVED TO APIGATEWAY ######################################################


# UI > (Api gateway) [POST] /volunteer/signup/ > (signupvolunteer) [POST] /volunteer/event/adduser/
# Get user status
# [GET] /user/{userID}
# Add volunteer - send request
# [POST] /volunteer/event/adduser/{userID}
@app.route("/volunteer/event/adduser", methods=['POST'])
def add_volunteer():
    # Get volunteer user data from request
    if request.is_json:
        try:
            data = request.get_json()

            userID = data.get('userID')
            volunteerEventID = data.get('volunteerEventID')
            
            if userID is None:
                return {'code': 400, 'data': {'msg':'Error no userID sent'}}, 400

            print("Getting user data...")
            print("----- Invoking user microservice to get user data -----")
            user_URL = f"http://user:{USER_HOST_PORT}/user/{str(userID)}"
            user_response_result = invoke_http(user_URL, method='GET')
            print("Result from user microservice:", user_response_result, "\n")

            if user_response_result['code'] in range(200,300):
                print("Received user data:", user_response_result['data'])
                data = user_response_result['data']
                data = {
                    "userID":userID,
                    "userName":data['userName'],
                    "contact":data['contact'],
                    "volunteerEventID":volunteerEventID
                }
                print("----- Invoking volunteer microservice to add volunteer data -----")
                volunteer_URL = f"http://volunteerevent:{VOLUNTEEREVENT_HOST_PORT}/volunteer/event/adduser"
                volunteer_response_result = invoke_http(volunteer_URL, method='POST', json=data)
                print("Result from volunteer microservice:", volunteer_response_result, "\n")
                return volunteer_response_result
            else:
                print("Error in getting user data:", user_response_result)
                return user_response_result
            
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            return jsonify({
                "code": 500,
                "message": "signupvolunteer.py internal error: " + ex_str
            }), 500 
        
    return jsonify({
        "code": 400,
        "message": "signupvolunteer.py bad request (Invalid JSON input): " + str(request.get_json())
    }), 400

# Execute this program if it is run as a main script
if __name__ == "__main__":
    print("signupvolunteer container is running...")
    while isServiceReady("user"):
        sleep(1)
    print("This is flask " + os.path.basename(__file__) + " for querying user status...")
    app.run(host="0.0.0.0", port=PORT, debug=True)

