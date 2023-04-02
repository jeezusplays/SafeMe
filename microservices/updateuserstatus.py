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

#from {pythonfile/service} import {function}
#import #{amqp_setup}
'''

import pika
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/safeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Placeholder for disaster microservice URL - May need reassignment later for port number
disaster_URL = "http://localhost:5002/disaster/update/user/"

# Update user status in disaster db through invoking disaster.py microservice
# Send status to disaster microservice disaster.py
# [POST] /user/status
@app.route("/user/status", methods=['POST'])
def send_user_status():
    """
    # Placeholder AMQP code before AMQP is fully configured
    # Send user status through AMQP
    message = json.dumps(user_status)
    status_code = request.get_json()["code"]
    
    if status_code == 200:

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, 
        routing_key="{userID}.{familyID}.status", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode=2))

        print("Sent user status through AMQP")
        print("\nUser status: ", user_status)

    """
    # Get user status from request
    if request.is_json:
        try:
            user_status = request.get_json()
            print("Received user status: ", user_status)

            # Add userid from userstatus json to disaster_URL
            disaster_URL = disaster_URL + str(user_status["userID"])

            # Invoke disaster microservice to update user status
            print("--- Invoking disaster microservice to update user status: ---")
            result = invoke_http(disaster_URL, method = "POST", json=user_status)
            print("Result: ", result)
            
            return jsonify(result), 200
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            return jsonify({
                "code": 500,
                "message": "update_user_status.py internal error: " + ex_str
            }), 500

    return jsonify({
        "code": 400,
        "message": "update_user_status.py bad request (Invalid JSON input): " + str(request.get_json())
    }), 400



''' 
Unsure if <int:userID> is needed in the route, need to test it out based on request from Alerts Websocket
Assumptions made: Alerts Websocket can extract userID from user_status json and send it as a parameter in the request
'''
# Update user status - send request
# [PUT] /disaster/update/user/{userID}
@app.route("/disaster/update/user/<int:userID>", methods=['PUT'])
def update_user_status_request():
    # Get user status from request
    if request.is_json:
        try:
            user_status = request.get_json()
            print("Received user status: ", user_status)

            # Update user status in disaster db
            print("--- Invoking disaster microservice to update user status: ---")
            disaster_URL = disaster_URL + str(user_status["userID"])
            result = invoke_http(disaster_URL, method = "PUT", json=user_status)
            print("Result: ", result)
            
            return jsonify(result), 200
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            return jsonify({
                "code": 500,
                "message": "update_user_status.py internal error: " + ex_str
            }), 500

    return jsonify({
        "code": 400,
        "message": "update_user_status.py bad request (Invalid JSON input): " + str(request.get_json())
    }), 400


# Send family member status through AMQP
# [AMQP] {userID}.{familyID}.status
# Has been merged with send_user_status() function

# Execute this program if it is run as a main script
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for querying user status...")
    app.run(host="0.0.0.0", port=5100, debug=True)

