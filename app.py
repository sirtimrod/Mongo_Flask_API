from flask import Flask
from flask_pymongo import PyMongo

from encoder import JSONEncoder


# Initialization the app application
app = Flask(__name__)
app.json_encoder = JSONEncoder
app.config["MONGO_URI"] = "mongodb://localhost:27017/storage"
mongo = PyMongo(app)

# Import all views and routes in main file
from views import *
