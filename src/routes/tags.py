from flask import Blueprint, abort

from src.service.tags import handleTagsGet, handleTagsGetOne

tags_bp = Blueprint('tags', __name__)


@tags_bp.route('/api/tags/read', methods=['GET'])
def userRead():
    """
    Escrever depois.
    """
    try:
        response = handleTagsGet()

        return response, 200
    except Exception as error:
        abort(500, description=str(error))


@tags_bp.route('/api/tags/read-one/<string:key>', methods=['GET'])
def userReadOne(key):
    """
    Escrever depois.
    """
    try:
        response = handleTagsGetOne(key)

        return response, 200
    except Exception as error:
        abort(500, description=str(error))
