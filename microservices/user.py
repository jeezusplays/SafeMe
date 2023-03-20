# Flask application to query db
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ


# Get user (Select one where userID == userID)

# Add location (Sdd location to location table)

# Get all user latest location (Select last location where userID == userID)

# Get family (Select * from users where familyID == familyID)

