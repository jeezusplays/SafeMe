# Flask application that query database
# Flask application to query db
import os
from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

DB_NAME = environ.get("VOLUNTEEREVENT_DB_NAME")
PORT = environ.get("VOLUNTEEREVENT_HOST_PORT")
print("This db name is: ",DB_NAME)
print("The port for this container: ",PORT)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root@db:3306/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Volunteer class with volunteerEventID, userID, userName, contact, timestamp with no ORM
class Volunteer(db.Model):
    __tablename__ = 'volunteer'

    volunteerEventID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, nullable=False)
    userName = db.Column(db.String(64), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, userID, userName, contact, timestamp):
        self.userID = userID
        self.userName = userName
        self.contact = contact
        self.timestamp = timestamp

    def json(self):
        return {"volunteerEventID": self.volunteerEventID, "userID": self.userID, "userName": self.userName, "contact": self.contact, "timestamp": self.timestamp}

# Volunteer event class with volunteerEventID, volunteerEventName, institute, disasterID with no ORM
class VolunteerEvent(db.Model):
    __tablename__ = 'volunteerevent'

    volunteerEventID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    volunteerEventName = db.Column(db.String(64), nullable=False)
    institute = db.Column(db.String(64), nullable=False)
    disasterID = db.Column(db.Integer, nullable=False)

    def __init__(self, volunteerEventName, institute, disasterID):
        self.volunteerEventName = volunteerEventName
        self.institute = institute
        self.disasterID = disasterID

    def json(self):
        return {"volunteerEventID": self.volunteerEventID, "volunteerEventName": self.volunteerEventName, "institute": self.institute, "disasterID": self.disasterID}

# Create volunteer event (Create volunteer event)
@app.route("/volunteer/event/create", methods=['POST'])
def create_volunteer_event():
    data = request.get_json()
    volunteerEvent = VolunteerEvent(**data)
    try:
        db.session.add(volunteerEvent)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the volunteer event."}), 500

    return jsonify(volunteerEvent.json()), 201

# Add volunteer (Add user to volunteer table)
@app.route("/volunteer/event/adduser", methods=['POST'])
def add_volunteer():
    data = request.get_json()
    volunteer = Volunteer(**data)
    try:
        db.session.add(volunteer)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred adding the volunteer."}), 500

    return jsonify(volunteer.json()), 201

# Get all volunteers (For UI) (select * from volunteers table)
@app.route("/volunteer", methods=['GET'])
def get_all_volunteers():
    return jsonify({"volunteers": [volunteer.json() for volunteer in Volunteer.query.all()]})

# Get volunteers by userID (For UI) (select * from volunteers table)
@app.route("/volunteer/<int:userID>", methods=['GET'])
def get_volunteers_by_userID(userID):
    volunteer = Volunteer.query.filter_by(userID=userID).first()
    if volunteer:
        return jsonify(volunteer.json())
    return jsonify({"message": "Volunteer not found."}), 404

# Get all volunteer event data (For UI) (select * from volunteer event)
@app.route("/volunteer/event", methods=['GET'])
def get_all_volunteer_events():
    return jsonify({"volunteerEvents": [volunteerEvent.json() for volunteerEvent in VolunteerEvent.query.all()]})

# Allows the service to be accessible from any other in the network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)