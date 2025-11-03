from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=2, max=50))