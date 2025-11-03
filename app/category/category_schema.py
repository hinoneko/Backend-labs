from marshmallow import Schema, fields, validate

class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    is_global = fields.Bool()
    user_id = fields.Str()