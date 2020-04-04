import os
from flask import Flask
from mongoengine import connect
from .util import JSONEncoder


#provisorio
mongo_host = 'mongodb://mongodb:27017/tc_status'

if __name__ == 'app':

    app = Flask(__name__)
    connect('campifarma_db', host=os.getenv('MONGO_HOST', mongo_host))

    app.json_encoder = JSONEncoder

    from app.controller import *
