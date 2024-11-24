from bson import ObjectId
from pymongo.errors import PyMongoError

from src.database.connection import get_database


def create(payload):
    """
    Escrever comentário.
    """
    database = get_database()

    try:
        cursor = database.services.insert_one(payload)

        if cursor is None:
            raise ValueError("Not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def read():
    """
    Escrever depois.
    """
    database = get_database()

    try:
        cursor = database.services.find({'is_active': True})

        if cursor is None:
            raise ValueError("Cursor not found")

        return list(cursor)
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def read_one(key):
    """
    Escrever depois.
    """
    database = get_database()

    try:
        cursor = database.services.find_one({'_id': ObjectId(key), 'is_active': True})

        if cursor is None:
            raise ValueError("Cursor not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def update_one(key, payload):
    """
    Escrever depois.
    """
    database = get_database()

    try:
        cursor = database.services.update_one({'_id': ObjectId(key)}, {'$set': payload})

        if cursor is None:
            raise ValueError("User not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def soft_delete(key):
    """
    Escrever depois.
    """
    database = get_database()

    try:
        cursor = database.services.update_one({'_id': ObjectId(key)}, {'$set': {'is_active': False}})

        if cursor is None:
            raise ValueError("Service not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def delete_one(key):
    """
    NÃO UTILIZAR SEM NECESSIDADE EXPLÍCITA.
    Remove o ponto de reparo do banco de dados com base no _id.
    Retorna uma mensagem de sucesso e o _id do usuário removido, ou erro.
    """
    database = get_database()

    try:
        cursor = database.services.delete_one({'_id': ObjectId(key)})

        if cursor is None:
            raise ValueError("Cursor not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")
