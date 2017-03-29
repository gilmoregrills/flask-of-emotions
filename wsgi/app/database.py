from app import app
from flask_pymongo import PyMongo
from flask import jsonify
import os

#app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

mongo = PyMongo(app)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
    return jsonify({'result' : mongo.db.collection_names()})

@app.route('/database/people', methods=['GET'])
def get_all_people():
    collection = mongo.db.people
    output = []
    for doc in collection.find():
        output.append({'who' : doc['Name'], 'cool?' : doc['cool']})
    return jsonify({'result' : output})
