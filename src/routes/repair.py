from flask import Blueprint, request, jsonify, abort
from src.service.repair import handleRepairCreate, handleRepairGet, handleRepairGetOne, handleRepairUpdateOne, handleRepairSoftDelete, handleRepairDeleteOne

repair_bp = Blueprint('repair', __name__)


@repair_bp.route('/api/repair/create', methods=['POST'])
def repairCreate():
    """
    Cria um anúncio de reparo no banco de dados.
    Passa o corpo da requisição (dados do serviço) para a função handler.
    Retorna uma mensagem de sucesso e o _id do objeto criado, ou erro.
    """
    try:
        response = handleRepairCreate(request.get_json())

        return jsonify({'message': "Service created successfully", '_id': str(response.inserted_id)}), 201
    except Exception as error:
        abort(500, description=str(error))


@repair_bp.route('/api/repair/read', methods=['GET'])
def userRead():
    """
    Escrever depois.
    """
    try:
        response = handleRepairGet()

        return response, 200
    except Exception as error:
        abort(500, description=str(error))


@repair_bp.route('/api/repair/read-one/<string:key>', methods=['GET'])
def userReadOne(key):
    """
    Escrever depois.
    """
    try:
        response = handleRepairGetOne(key)

        return response, 200
    except Exception as error:
        abort(500, description=str(error))


@repair_bp.route('/api/repair/update-one/<string:key>', methods=['PUT'])
def repairUpdateOne(key):
    """
    Escrever depois.
    """
    try:
        response = handleRepairUpdateOne(key, request.get_json())

        return ({'message': "Repair point updated successfully", '_id': key}), 200
    except Exception as error:
        abort(500, description=str(error))


@repair_bp.route('/api/repair/soft-delete/<string:key>', methods=['PATCH'])
def repairSoftDeleteOne(key):
    """
    Escrever depois.
    """
    try:
        response = handleRepairSoftDelete(key)

        return ({'message': "Repair point soft-deleted successfully", '_id': key}), 200
    except Exception as error:
        abort(500, description=str(error))


@repair_bp.route('/api/repair/delete-one/<string:key>', methods=['DELETE'])
def repairDeleteOne(key):
    """
    Remove o usuário do banco de dados com base no _id.
    NÃO DEVERÁ SER UTILIZADO SEM NECESSIDADE EXPLÍCITA.
    Retorna uma mensagem de sucesso e o _id do usuário removido, ou erro.
    """
    try:
        response = handleRepairDeleteOne(key)

        return ({'message': "Repair point hard-deleted successfully", '_id': key}), 200
    except Exception as error:
        abort(500, description=str(error))
