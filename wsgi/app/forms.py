from flask_wtf import Form
from wtforms import TextField, validators

class MessageForm(Form):
   message = TextField(u'tfw u realise that maybe u have spent too long online when u need a computer to tell u if a message is good or not', [validators.optional(), validators.length(max=200)])



