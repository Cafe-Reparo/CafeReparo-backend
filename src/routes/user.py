from flask import Blueprint, request, abort, jsonify
from src.service.user import handleUserCreate, handleUserGet, handleUserGetOne, handleUserUpdateOne, handleUserDeleteOne, handleUserSoftDeleteOne

user_bp = Blueprint('user', __name__)


@user_bp.route('/api/user/create', methods=['POST'])
def userCreate():
    """
    Cria um usuário no banco de dados.
    Passa o corpo da requisição (dados do novo usuário) para a função handler.
    Retorna uma mensagem de sucesso e o _id do usuário criado, ou erro.
    """
    try:
        response = handleUserCreate(request.get_json())

        return jsonify({'message': "User created successfully", '_id': str(response.inserted_id)}), 201
    except Exception as error:
        abort(500, description=str(error))


@user_bp.route('/api/user/read', methods=['GET'])
def userRead():
    """
    Busca todos os usuários do banco de dados.
    Retorna uma lista com todos os usuários ativos, ou erro.
    """
    try:
        response = handleUserGet()

        return response, 200
    except Exception as error:
        abort(500, description=str(error))


@user_bp.route('/api/user/read-one/<string:key>', methods=['GET'])
def userReadOne(key):
    """
    Busca um usuário do banco de dados com base em um parâmetro.
    Utiliza o ObjectId (_id) como parâmetro.
    Retorna o usuário encontrado, ou erro.
    """
    try:
        response = handleUserGetOne(key)

        return response, 200
    except Exception as error:
        abort(500, description=str(error))


@user_bp.route('/api/user/update-one/<string:key>', methods=['PUT'])
def userUpdateOne(key):
    """
    Atualiza um usuário no banco de dados com base em um parâmetro.
    Passa o corpo da requisição (dados do usuário atualizado) para a função handler.
    Retorna uma mensagem de sucesso e o _id do usuário atualizado, ou erro.
    """
    try:
        response = handleUserUpdateOne(key, request.get_json())

        return ({"message": "User updated successfully", "_id": key}), 200
    except Exception as error:
        abort(500, description=str(error))


@user_bp.route('/api/user/soft-delete-one/<string:key>', methods=['PATCH'])
def userSoftDeleteOne(key):
    """
    Marca o usuário para ser ignorado em qualquer operação futura.
    Altera o campo is_active do _id enviado para false.
    Retorna uma mensagem de sucesso e o _id do usuário atualizado, ou erro.
    """
    try:
        response = handleUserSoftDeleteOne(key)

        return ({"message": "User soft-deleted successfully", "_id": key}), 200
    except Exception as error:
        abort(500, description=str(error))


@user_bp.route('/api/user/delete-one/<string:key>', methods=['DELETE'])
def userDeleteOne(key):
    """
    Remove o usuário do banco de dados com base no _id.
    NÃO DEVERÁ SER UTILIZADO SEM NECESSIDADE EXPLÍCITA.
    Retorna uma mensagem de sucesso e o _id do usuário removido, ou erro.
    """
    try:
        response = handleUserDeleteOne(key)

        return ({'message': "User hard-deleted successfully", '_id': key}), 200
    except Exception as error:
        abort(500, description=str(error))
