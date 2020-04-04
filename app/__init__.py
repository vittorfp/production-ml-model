from flask import Flask
from .util import JSONEncoder


if __name__ == 'app':
    app = Flask(__name__)
    app.json_encoder = JSONEncoder
    from app.controller import *
