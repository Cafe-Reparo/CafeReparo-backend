import string
from marshmallow import Schema, fields, validate

from src.utils.schemas.contactSchema import ContactSchema

ALPHABET = string.ascii_lowercase + string.ascii_uppercase


# Objeto para validar o campo de reparo
class RepairSchema(Schema):
    name = fields.Str(validate=validate.And(validate.Length(min=3, max=20)), required=True)
    description = fields.Str(validate=validate.And(validate.Length(min=1, max=200)))
    email = fields.Email(required=True)
    phone = fields.List(fields.Str(validate=validate.And(validate.Length(min=1, max=16))))
    contacts = fields.List(fields.Nested(ContactSchema))
    tags = fields.List(fields.Str(validate=validate.And(validate.Length(min=1, max=20))))
    creation = fields.Raw()
    last_validated = fields.Raw(default="")
    is_validated = fields.Boolean(default=False)
    is_active = fields.Boolean(default=True)
    owner_id = fields.Raw(required=True)
