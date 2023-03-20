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

# User class with userID, userName, familyID, age, country, email, contact
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


# Get all users from db
@app.route("/user", methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.json())
    return jsonify(result)


# Get user (Select one where userID == userID)

# Add location (Sdd location to location table)

# Get all user latest location (Select last location where userID == userID)

# Get family (Select * from users where familyID == familyID)

