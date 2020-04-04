from datetime import datetime
import json
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    ''' Extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
