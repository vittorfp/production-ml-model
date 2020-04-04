import json
from flask import jsonify, request

from app import app
from app.schema import location_schema
from app.util import validate_input


# /predict
@app.route('/predict', methods=['GET'])
def predict():

    input_data = validate_input(location_schema, dict(request.args))
    if isinstance(input_data, tuple):
        return input_data

    return jsonify({'error': 'Not implemented'}), 500
