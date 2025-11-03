from marshmallow import Schema, fields, validate

class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01))
    user_id = fields.Str(required=True)
    category_id = fields.Str()
    created_at = fields.DateTime(dump_only=True)