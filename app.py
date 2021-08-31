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

# [
#     {
#         name: 'iPhone 12',
#         description: "The iPhone 12 and iPhone 12 mini are part of Apple's latest generation of smartphones, offering OLED displays, 5G connectivity, the A14 chip for better performance, improved cameras, and MagSafe, all in a new, squared-off design.",
#         parameters: {weight: 0.732, price: "500$", colore: 'blue', memory: '256Gb'}
#     },
# {
#         'name': 'iPhone 12',
#         'description': "The iPhone 12 and iPhone 12 mini are part of Apple's latest generation of smartphones, offering OLED displays, 5G connectivity, the A14 chip for better performance, improved cameras, and MagSafe, all in a new, squared-off design.",
#         'parameters': {weight: 0.732, price: "500$", colore: 'green', memory: '128Gb'}
#     },
# {
#         'name': 'MiBand 6',
#         'description': "The Mi Band 6 works with the Mi Fit app and the core functionality remains unchanged - it can do heart-rate measurements, sleep tracking, sport tracking, show notifications, act as a camera shutter, control your default music player, has the usual alarm/timer/stopwatch functions.",
#         'parameters': {weight: 0.120, price: "25$", colore: 'black', autonomy: '168h'}
#     },
# {
#         'name': 'Macbook PRO',
#         'description': "Apple MacBook Pro is a macOS laptop with a 13.30-inch display that has a resolution of 2560x1600 pixels. It is powered by a Core i5 processor and it comes with 12GB of RAM. The Apple MacBook Pro packs 512GB of SSD storage.",
#         'parameters': {weight: 1.33, price: "1200$", colore: 'grey', SSD: '512Gb'}
#     }
# ]
