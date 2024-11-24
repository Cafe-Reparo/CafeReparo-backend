from datetime import datetime, timezone
from bson import ObjectId
from marshmallow import ValidationError

from src.utils.conversion.dateFormat import convertToIso
from src.utils.schemas.repairSchema import RepairSchema
from src.database.repair import create, read, read_one, update_one, soft_delete, delete_one
from src.utils.validate import validate


def handleRepairCreate(formData):
    try:
        formData['creation'] = datetime.now(tz=timezone.utc)
        formData['owner_id'] = ObjectId(formData['owner_id'])
        formData['last_validated'] = ""
        formData['is_validated'] = False
        formData['is_active'] = True

        payload = validate(formData, RepairSchema)

        return create(payload)
    except ValidationError as validation_error:
        raise ValidationError(f"Invalid formData: {validation_error}")


def handleRepairGet():
    """
    Escrever depois.
    """
    try:
        response = read()

        for repair in response:
            repair['_id'] = str(repair['_id'])
            repair['creation'] = convertToIso(repair['creation'])
            repair['owner_id'] = str(repair['owner_id'])

            if repair['last_validated'] != "":
                repair['last_validated'] = convertToIso(repair['last_validated'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleRepairGetOne(key):
    """
    Escrever depois.
    """
    try:
        response = read_one(key)

        response['_id'] = str(response['_id'])
        response['creation'] = convertToIso(response['creation'])
        response['owner_id'] = str(response['owner_id'])

        if response['last_validated'] != "":
            response['last_validated'] = convertToIso(response['last_validated'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleRepairUpdateOne(key, formData):
    """
    Escrever depois.
    """
    try:
        payload = validate(formData, RepairSchema)

        return update_one(key, payload)
    except ValidationError as validation_error:
        raise ValueError(f"Invalid data: {validation_error}")


def handleRepairSoftDelete(key):
    """
    Escrever depois.
    """
    try:
        return soft_delete(key)
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleRepairDeleteOne(key):
    """
    NÃO DEVERÁ SER UTILIZADO SEM NECESSIDADE EXPLÍCITA.
    Remove o ponto de reparo do banco de dados com base no _id.
    Retorna a resposta da operação enviada pelo banco de dados, ou erro.
    """
    try:
        return delete_one(key)
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")
