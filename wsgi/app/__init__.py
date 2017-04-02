from flask import Flask 

app = Flask(__name__)

#this is will be changed once app is deployed
app.secret_key = ''

from app import views

