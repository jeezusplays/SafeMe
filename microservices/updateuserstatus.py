# Flask application to query db
import os, sys
import requests
from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#from {pythonfile/service} import {function}

#import #{amqp_setup}
import pika
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/safeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Update user status in disaster db
# Send status
# [POST] /user/status
@app.route("/user/status", methods=['POST'])
def update_user_status():
    data = request.get_json()
    userID = data['userID']
    status = data['status']
    return jsonify({"message": "User status updated successfully."}), 200

# Update user status - send request
# [PUT] /disaster/update/user/{userID}
@app.route("/disaster/update/user/<int:userID>", methods=['PUT'])
def update_user_status_request(userID):
    data = request.get_json()
    status = data['status']
    return jsonify({"message": "User status updated successfully."}), 200

# Send family member status through AMQP
# [AMQP] {userID}.{familyID}.status


