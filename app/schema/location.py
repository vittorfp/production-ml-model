from marshmallow import Schema, fields
from marshmallow.validate import Range


class Location(Schema):
    class Meta:
        unknown = 'raise'

    lat = fields.Number(required=True, validate=Range(min=-90, max=90))
    lon = fields.Number(required=True, validate=Range(min=-180, max=180))


location_schema = Location()
