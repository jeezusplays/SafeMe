# Flask application to query db
import os, sys
import requests
from os import environ
from invokes import invoke_http

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

'''
AMQP Setup required for sending family member status, not operational yet until AMQP is fully configured

#import #{amqp_setup}
'''

import pika
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/safeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Get all volunteer event data
# (For UI)
# [GET] /volunteer/event
# Return all volunteer event data from calling volunteer event microservice volunteer.py with invokes.py to parse json data
@app.route("/volunteer/event", methods=['GET'])
def get_all_volunteer_event():
    print("Getting all volunteer event data...")
    response = invoke_http("http://localhost:5003/volunteer/event", method='GET')
    return response

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
            print("Getting user data...")
            print("----- Invoking user microservice to get user data -----")
            user_response_result = invoke_http("http://localhost:5001/user/" + str(data['userID']), method='GET')
            print("Result from user microservice:", user_response_result)
            if user_response_result['code'] == 200:
                print("Received volunteer data:", data)
                print("----- Invoking volunteer microservice to add volunteer data -----")
                volunteer_URL = "http://localhost:5003/volunteer/event/adduser/" + str(data["userID"])
                volunteer_response_result = invoke_http(volunteer_URL, method='POST', json=data)
                print("Result from volunteer microservice:", volunteer_response_result)
                return jsonify(volunteer_response_result), 200
            else:
                print("Error in getting user data:", user_response_result)
                return jsonify(user_response_result), 400
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
    print("This is flask " + os.path.basename(__file__) + " for querying user status...")
    app.run(host="0.0.0.0", port=5200, debug=True)

