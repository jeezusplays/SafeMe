# Flask application to query db
import os, sys
import json

from pprint import pprint
from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_cors import CORS
from amqp_helper import Rabbitmq

'''
AMQP Setup required for sending disaster data, not operational yet until AMQP is fully configured
#import #{amqp_setup}
'''

app = Flask(__name__)
CORS(app)

# Get GDAC alert
# gdac.alert
def alertCallback(ch, method, properties, body):
    data = json.loads(body)
    pprint(data)
    # print("Received message:", data)

    pass

def main():
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('gdacalert',alertCallback)

# Send localised alerts
# [AMQP] {country}.{city}.alert

# Get all user latest location - send request
# [GET] /location/latest
@app.route("/location/latest", methods=["GET"])
def get_all_users_latest_location():
    print("Getting all users latest location...")
    # Get all users latest location
    response = invoke_http("http://localhost:5001/location/latest", method="GET")
    print("Response: ", response)
    return response

# Create disaster - send request
# [POST] /disaster/new
@app.route("/disaster/new", methods=["POST"])
def create_disaster():
    if request.is_json:
        try:
            print("Creating disaster...")
            print("----- Invoking disaster microservice to get user data -----")
            data = request.get_json()
            # Create disaster
            response = invoke_http("http://localhost:5002/disaster/new", method="POST", json=data)
            print("Result from disaster microservice: ", response)
            return response
        
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            return jsonify({
                "code": 500,
                "message": "createdisaster.py internal error: " + ex_str
            }), 500 
    
    return jsonify({
        "code": 400,
        "message": "createdisaster.py bad request (Invalid JSON input): " + str(request.get_json())
    }), 400


# Execute this program if it is run as a main script
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for querying user status...")
    app.run(host="0.0.0.0", port=5200, debug=True)


