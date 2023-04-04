# Flask application that query database
# Flask application to query db
import os
from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from datetime import datetime
# import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/safeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Disaster class with disasterID, disasterName, country, city, lat, long, disasterSeverityLevel with no ORM
class Disaster(db.Model):
    __tablename__ = 'disaster'

    disasterID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disasterName = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    lat = db.Column(db.Float(precision=3), nullable=False)
    long = db.Column(db.Float(precision=3), nullable=False)
    disasterSeverityLevel = db.Column(db.String(64), nullable=False)
    disasterTimestamp = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, disasterName, country, city, lat, long, disasterSeverityLevel, disasterTimestamp):
        self.disasterName = disasterName
        self.country = country
        self.city = city
        self.lat = lat
        self.long = long
        self.disasterSeverityLevel = disasterSeverityLevel
        self.disasterTimestamp = disasterTimestamp

    def json(self):
        return {"disasterID": self.disasterID, "disasterName": self.disasterName, "country": self.country, "city": self.city, "lat": self.lat, "long": self.long, "disasterSeverityLevel": self.disasterSeverityLevel, "disasterTimestamp": self.disasterTimestamp}

# Affected user class with affectedUsersID, disasterID, userID, userName, status, contact with no ORM
class AffectedUser(db.Model):
    __tablename__ = 'affectedusers'

    affectedUsersID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disasterID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    userName = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    contact = db.Column(db.Integer, nullable=False)

    def __init__(self, disasterID, userID, userName, status, contact):
        self.disasterID = disasterID
        self.userID = userID
        self.userName = userName
        self.status = status
        self.contact = contact

    def json(self):
        return {"affectedUsersID": self.affectedUsersID, "disasterID": self.disasterID, "userID": self.userID, "userName": self.userName, "status": self.status, "contact": self.contact}

# Create or add disaster (add disaster to disaster table)
@app.route("/disaster/new", methods=['POST'])
def create_disaster():
    data = request.get_json()
    disaster = Disaster(**data)
    try:
        db.session.add(disaster)
        db.session.commit()
    except:
        return jsonify({"code": 500, "data": {"message": "An error occurred creating the disaster."}}), 500

    return jsonify({"code": 201, "data": disaster.json()}), 201

# Add affected users (add users to affecteduser table)
@app.route("/affecteduser", methods=['POST'])
def create_affected_user():
    data = request.get_json()
    affected_user = AffectedUser(**data)
    try:
        db.session.add(affected_user)
        db.session.commit()
    except:
        return jsonify({"code": 500, "data": {"message": "An error occurred adding the affected user."}}), 500

    return jsonify({"code": 201, "data": affected_user.json()}), 201

# Update user status (Update user from affected_user table by userID)
@app.route("/disaster/update/user/<int:affectedUsersID>", methods=['PUT'])
def update_user_status(affectedUsersID):
    affected_user = AffectedUser.query.filter_by(affectedUsersID=affectedUsersID).first()
    if affected_user:
        data = request.get_json()   
        affected_user.status = data['status']
        try:
            db.session.commit()
        except:
            return jsonify({"code": 500, "message": "An error occurred updating the affected user."}), 500

        return jsonify({"code": 200, "data": affected_user.json()}), 200

    return jsonify({"message": "Affected user not found."}), 404

# Get user status  (select * from affected_users table)
@app.route("/affected/<int:disasterID>", methods=['GET'])
def get_user_status(disasterID):
    affected_user = AffectedUser.query.filter_by(disasterID=disasterID).all()
    if affected_user:
        return jsonify({"code": 200, "data": [affected_user.json() for affected_user in affected_user]}), 200

    return jsonify({"message": "Affected user not found."}), 404

# Get all user status  (select * from affected_users table)
@app.route("/affected", methods=['GET'])
def get_all_user_status():
    affected_user = AffectedUser.query.all()
    if affected_user:
        return jsonify({"code": 200, "data": [affected_user.json() for affected_user in affected_user]}), 200

    return jsonify({"message": "Affected user not found."}), 404

# Allows the service to be accessible from any other in the network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)