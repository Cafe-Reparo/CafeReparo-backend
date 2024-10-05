from datetime import datetime
from flask import Blueprint, request, abort
from pymongo.errors import PyMongoError
from marshmallow import Schema, fields
from src.database.user import *

user_bp = Blueprint('user', __name__)


class UserSchema(Schema):
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    birthday = fields.Dict(keys=fields.Str(required=True), values=fields.Str(required=True))
    creation = fields.Dict(keys=fields.Str(required=True), values=fields.Str(required=True))
    picture = fields.Str()
    is_admin = fields.Boolean(default=False)
    is_active = fields.Boolean(default=True)


schema = UserSchema()


def validate(data):
    return schema.dump(data)


# cria um usuário
@user_bp.route('/api/user/create', methods=['POST'])
def userCreate():
    try:
        payload = validate(request.get_json())
        response = create(payload)

        return response, 201
    except ValueError as value_error:
        abort(400, description=str(value_error))


# retorna todos os usuários
@user_bp.route('/api/user/read', methods=['GET'])
def userRead():
    response = read()

    return response, 200


# retorna um usuário com base no _id
@user_bp.route('/api/user/read-one/<string:key>', methods=['GET'])
def userReadOne(key):
    try:
        response = read_one(key)

        return response, 200
    except ValueError as value_error:
        abort(404, description=str(value_error))
    except PyMongoError as db_error:
        abort(500, description=f"Database error: {str(db_error)}")
    except Exception as error:
        abort(500, description="An internal error occurred.")


# atualiza um usuário com base no _id
@user_bp.route('/api/user/update-one/<string:key>', methods=['PUT'])
def userUpdateOne(key):
    payload = validate(request.get_json())

    response = update_one(key, payload)

    return response, 200


# soft delete em um usuário com base no _id
@user_bp.route('/api/user/soft-delete-one/<string:key>', methods=['PATCH'])
def userSoftDeleteOne(key):
    response = soft_delete_one(key)

    return response, 200


# deleta um usuário com base no _id
@user_bp.route('/api/user/delete-one/<string:key>', methods=['DELETE'])
def userDeleteOne(key):
    response = delete_one(key)

    return response, 200
