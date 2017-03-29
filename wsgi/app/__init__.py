from flask import Flask 

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = 'ZoltaR2'

from app import views

