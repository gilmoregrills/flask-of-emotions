from flask import Flask 

app = Flask(__name__)

#this is will be changed once app is deployed
app.secret_key = 'localsecrets'

from app import views

