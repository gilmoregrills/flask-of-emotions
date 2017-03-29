from app import app
from flask_pymongo import PyMongo
from flask import jsonify
import os

app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + app.config['MONGO_DBNAME']

mongo = PyMongo(app)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
    return jsonify({'result' : mongo.db.collection_names()})

@app.route('/database/people', methods=['GET'])
def get_all_people():
    collection1 = mongo.db.people.coolPeople
    collection2 = mongo.db.people.lamePeople
    output = []
    for doc in collection1.find():
        output.append(doc)
    for doc in collection2.find():
        output.append(doc)
    return jsonify({'result' : output})
