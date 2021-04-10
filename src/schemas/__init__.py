from marshmallow import fields, Schema

class BootcampListSchema(Schema):
    """
    Bootcamp List Schema
    """
    id = fields.Int(required=True)
    name = fields.Str(required=True)
