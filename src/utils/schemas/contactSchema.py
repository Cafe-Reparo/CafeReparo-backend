from marshmallow import Schema, fields, validate


class ContactSchema(Schema):
    platform = fields.Str(validate=validate.And(validate.Length(min=1, max=20)), required=True)
    link = fields.Str(validate=validate.And(validate.Length(min=1, max=100)), required=True)
