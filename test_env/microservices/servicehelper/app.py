# Flask application to query db
from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS

import json

PORT = environ.get("SERVICEHELPER_HOST_PORT")
print("The port for this container: ",PORT)

app = Flask(__name__)
CORS(app)

# get ready services
@app.route("/services/ready/<string:servicename>", methods=['GET'])
def get_ready_services(servicename):
    e = "Error getting service status"
    if servicename is not None:
        if servicename in service_set:
            return json.dumps({"code": 200, "message": True}), 200
        else:
            return json.dumps({"code": 200, "message": False}), 200
    else:
        e = "service name input is None"
    return json.dumps({"code": 500, "message": e}), 500

@app.route("/services/ready/set/<string:servicename>", methods=['GET'])
def set_ready_services(servicename):
    e = "Error setting service status"
    if servicename is not None:
        service_set.add(servicename)
        return json.dumps({"code": 200, "message": "Successfully posted status"}), 200
    else:
        e = "service name input is None"
    return json.dumps({"code": 500, "message": e}), 500

if __name__ == "__main__":
    global service_set
    service_set=set()
    app.run(host='0.0.0.0', port=PORT)
