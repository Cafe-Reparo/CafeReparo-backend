from datetime import datetime, timezone
from marshmallow import ValidationError
from src.database.user import create, read, read_one, update_one, soft_delete_one, delete_one
from src.utils.conversion.dateFormat import convertToDatetime, convertToIso
from src.utils.schemas.userSchema import UserSchema
from src.utils.validate import validate


def handleUserCreate(formformData):
    """
    Cria um usuário no banco de dados.
    Transforma os dados nos formatos esperados pelo MongoDB, valida-os e os passa para a função de criação.
    Retorna a resposta do banco de dados, ou erro.
    """
    try:
        formformData['birthday'] = convertToDatetime(formformData['birthday'])
        formformData['creation'] = datetime.now(tz=timezone.utc)
        formformData['picture'] = dict(formData='', subType='00')
        formformData['is_admin'] = False
        formformData['is_active'] = True

        payload = validate(formformData, UserSchema)

        return create(payload)
    except ValidationError as validation_error:
        raise ValidationError(f"Invalid formData: {validation_error}")


def handleUserGet():
    """
    Busca todos os usuários do banco de dados.
    Garante que todos os campos sejam compatíveis com formato JSON.
    Retorna uma lista com todos os usuários ativos, ou erro.
    """
    try:
        response = read()

        for user in response:
            user['_id'] = str(user['_id'])
            user['birthday'] = convertToIso(user['birthday'])
            user['creation'] = convertToIso(user['creation'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleUserGetOne(key):
    """
    Busca um usuário do banco de dados com base em um parâmetro.
    Garante que todos os campos sejam compatíveis com formato JSON.
    Retorna o usuário encontrado, ou erro.
    """
    try:
        response = read_one(key)

        response['_id'] = str(response['_id'])
        response['birthday'] = convertToIso(response['birthday'])
        response['creation'] = convertToIso(response['creation'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleUserUpdateOne(key, formData):
    """
    Atualiza um usuário no banco de dados com base em um parâmetro.
    Garante que todos os campos sejam compatíveis com formato JSON.
    Retorna a resposta da operação enviada pelo banco de dados, ou erro.
    """
    try:
        formData['birthday'] = convertToDatetime(formData['birthday'])

        payload = validate(formData, UserSchema)

        return update_one(key, payload)
    except ValidationError as validation_error:
        raise ValueError(f'Invalid data: {validation_error}')


def handleUserSoftDeleteOne(key):
    """
    Desativa um usuário no banco de dados com base no _id.
    Altera o campo is_active do _id enviado para false.
    Retorna a resposta da operação enviada pelo banco de dados, ou erro.
    """
    try:
        return soft_delete_one(key)
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleUserDeleteOne(key):
    """
    Remove o usuário do banco de dados com base no _id.
    NÃO DEVERÁ SER UTILIZADO SEM NECESSIDADE EXPLÍCITA.
    Retorna a resposta da operação enviada pelo banco de dados, ou erro.
    """
    try:
        return delete_one(key)
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")
