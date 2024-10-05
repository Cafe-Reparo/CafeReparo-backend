from marshmallow import ValidationError


def validate(payload, schema):
    """
    Valida um payload com base em um schema.
    """
    try:
        return schema().load(payload)
    except ValidationError as validation_error:
        raise ValueError(f'Invalid data: {validation_error}')
