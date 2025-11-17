from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    password = fields.Str(required=True, validate=validate.Length(min=6))


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)