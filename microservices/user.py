# Flask application to query db
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/safeme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# User class with userID, userName, familyID, age, country, email, contact with no ORM
class User(db.Model):
    __tablename__ = 'user'

    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64), nullable=False)
    familyID = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    contact = db.Column(db.Integer, nullable=False)

    def __init__(self, userID, userName, familyID, age, country, email, contact):
        self.userID = userID
        self.userName = userName
        self.familyID = familyID
        self.age = age
        self.country = country
        self.email = email
        self.contact = contact

    def json(self):
        return {"userID": self.userID, "userName": self.userName, "familyID": self.familyID, "age": self.age, "country": self.country, "email": self.email, "contact": self.contact}

# User class using Object Relational Mapping (ORM) with userID, userName, familyID, age, country, email, contact
# class User(db.Model):
#     __tablename__ = 'user'
#     userID = db.Column(db.Integer, primary_key=True)
#     userName = db.Column(db.String(64), nullable=False)
#     familyID = db.Column(db.Integer, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     country = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(64), nullable=False)
#     contact = db.Column(db.Integer, nullable=False)
#     location = db.relationship('Location', backref=db.backref('user', lazy=True))

# Location class with locationID, userID, country, city, lat, long, timestamp with no ORM
class Location(db.Model):
    __tablename__ = 'location'

    locationID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Date, nullable=False) # May need to change to DateTime

    def __init__(self, locationID, userID, country, city, lat, long, timestamp):
        self.locationID = locationID
        self.userID = userID
        self.country = country
        self.city = city
        self.lat = lat
        self.long = long
        self.timestamp = timestamp

    def json(self):
        return {"locationID": self.locationID, "userID": self.userID, "country": self.country, "city": self.city, "lat": self.lat, "long": self.long, "timestamp": self.timestamp}

# Location class using Object Relational Mapping (ORM) with locationID, userID, country, city, lat, long, timestamp
# class Location(db.Model):
#     __tablename__ = 'location'
#     locationID = db.Column(db.Integer, primary_key=True)
#     userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)
#     country = db.Column(db.String(64), nullable=False)
#     city = db.Column(db.String(64), nullable=False)
#     lat = db.Column(db.Float, nullable=False)
#     long = db.Column(db.Float, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False)
#     user = db.relationship('User', backref=db.backref('location', lazy=True))

# Get all users from db
@app.route("/user", methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    # Check if length of users is 0
    if len(users) != 0:
        for user in users:
            result.append(user.json())
        return jsonify({"code": 200, "data": result})
    else:
        return jsonify({"code": 404, "message": "There are no users"}), 404

# Get user (Select one where userID == userID)
@app.route("/user/<int:userID>", methods=['GET'])
def get_user(userID):
    user = User.query.filter_by(userID=userID).first()
    if user:
        return jsonify({"code": 200, "data": user.json()})
    else:
        return jsonify({"code": 404, "message": "User not found"}), 404

# Add location (Add user's location information through userID to location table)
@app.route("/location/", methods=['POST'])
def add_location():
    data = request.get_json()
    location = Location(data['locationID'], data['userID'], data['country'], data['city'], data['lat'], data['long'], data['timestamp'])
    try:
        db.session.add(location)
        db.session.commit()
    except:
        return jsonify({"code": 500, "data": {"message": "An error occurred while adding the location."}}), 500
    return jsonify({"code": 201, "data": location.json()}), 201

# Get all users latest location (Select last location where userID == userID)
@app.route("/location/latest", methods=['GET'])
def get_all_users_latest_location():
    user_loc = Location.query.order_by(Location.timestamp.desc()).group_by(Location.userID).all()
    result = []
    # Check if length of users is 0
    if len(user_loc) != 0:
        for user in user_loc:
            result.append(user.json())
        return jsonify({"code": 200, "data": result})
    else:
        return jsonify({"code": 404, "message": "There are no users"}), 404

# Get family (Select * from users where familyID == familyID)
@app.route("/user/family/familyID", methods=['GET'])
def get_family():
    data = request.get_json()
    family = User.query.filter_by(familyID=data['familyID']).all()
    result = []
    # Check if length of users is 0
    if len(family) != 0:
        for user in family:
            result.append(user.json())
        return jsonify({"code": 200, "data": result})
    else:
        return jsonify({"code": 404, "message": "There are no users"}), 404

# Allows the service to be accessible from any other in the network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)