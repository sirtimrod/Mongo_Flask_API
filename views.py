from flask import request, jsonify

from app import app, mongo
from bson.objectid import ObjectId


# The method accepts JSON with a name and a parameter, and displays a list of names that match the data
@app.route('/products', methods=['GET'])
def get_product():
    data = []
    if 'name' in request.json and 'parameters' in request.json:
        param_key, param_value = tuple(*request.json['parameters'].items())
        for doc in mongo.db.shop.find({'name': request.json['name'],
                                       f'parameters.{param_key}': param_value}):
            data.append(doc['name'])

    if 'name' not in request.json:
        param_key, param_value = tuple(*request.json['parameters'].items())
        for doc in mongo.db.shop.find({f'parameters.{param_key}': param_value}):
            data.append(doc['name'])

    if 'parameters' not in request.json:
        for doc in mongo.db.shop.find({'name': request.json['name']}):
            data.append(doc['name'])

    return jsonify(result=data), 200


# The method accepts JSON with id and returns all product data
@app.route('/details', methods=['GET'])
def get_details():
    data = mongo.db.shop.find_one({'_id': ObjectId(request.json['id'])})
    return jsonify(result=data), 200


# The method accepts JSON with the data of the new product and creates a new record in the DB
@app.route('/create', methods=['POST'])
def create_new():
    new_product_id = mongo.db.shop.insert({'name': request.json['name'],
                                           'description': request.json['description'],
                                           'parameters': request.json['parameters']})
    new_product = mongo.db.shop.find_one({'_id': new_product_id})
    return jsonify(result=new_product), 201
