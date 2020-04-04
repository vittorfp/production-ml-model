from json.decoder import JSONDecodeError
from flask import jsonify
from marshmallow import ValidationError


def validate_input(schema, data):
    if not len(data):
        # app.logger.debug('Validation error: Empty body.')
        return jsonify({'error': 'Validation error: Empty body.'}), 400

    try:
        body = schema.load(data)
    except ValidationError as err:
        # app.logger.debug('Validation error: %s %s.' % (data, err.messages))
        return jsonify({'error': err.messages}), 422
    except JSONDecodeError:
        return jsonify({'error': 'Malformed body. JSONDecodeError'}), 400

    return body
