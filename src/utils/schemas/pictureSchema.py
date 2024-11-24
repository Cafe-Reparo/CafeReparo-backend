from marshmallow import Schema, fields


class PictureSchema(Schema):
    data = fields.Str(required=True)
    subType = fields.Str(missing="00")
