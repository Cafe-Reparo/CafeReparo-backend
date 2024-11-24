import string
from marshmallow import Schema, fields, validate

ALPHABET = string.ascii_lowercase + string.ascii_uppercase


# Objeto para validar o campo de usuário
class UserSchema(Schema):
    name = fields.Str(validate=validate.And(validate.Length(min=3, max=20), validate.ContainsOnly(ALPHABET)), required=True)
    surname = fields.Str(validate=validate.And(validate.Length(min=3, max=20), validate.ContainsOnly(ALPHABET)), required=True)
    email = fields.Email(required=True)
    password = fields.Str(validate=validate.Length(min=6, max=40), required=True)
    birthday = fields.Raw(required=True)
    creation = fields.Raw()
    picture = fields.Raw(default=dict(formData='', subType='00'))
    is_admin = fields.Boolean(default=False)
    is_active = fields.Boolean(default=True)
