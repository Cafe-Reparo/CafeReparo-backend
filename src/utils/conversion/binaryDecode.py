import base64
from bson import Binary
from marshmallow import post_load


@post_load
def decodeBinary(payload):
    """
    Decodifica um binário recebido.
    """
    binary = base64.b64decode(payload['data'])
    subtype = int(payload.get('subType', '00'), 16)
    payload['data'] = Binary(binary, subtype=subtype)

    return payload
