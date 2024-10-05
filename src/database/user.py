from bson import ObjectId
from pymongo import errors
from src.database.connection import get_database


# registra um usuário no banco de dados
def create(payload):
    database = get_database()

    try:
        cursor = database.users.insert_one(payload)

        return cursor
    except Exception as error:
        raise Exception("Erro: ", error)


# retorna lista com todos os usuários
def read():
    database = get_database()

    try:
        cursor = database.users.find({'is_active': True}, {"_id": 0, "picture": 0, "is_active": 0})

        return list(cursor)
    except Exception as error:
        raise Exception("Erro: ", error)


# retorna um usuário com base no _id
def read_one(key):
    database = get_database()

    try:
        cursor = database.users.find_one({"_id": ObjectId(key), 'is_active': True}, {"_id": 0, "picture": 0, "is_active": 0})

        if cursor is None:
            raise ValueError("User not found")

        return cursor
    except errors.PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


# edita um usuário com base no _id
def update_one(key, payload):
    database = get_database()

    try:
        cursor = database.users.update_one({"_id": ObjectId(key)}, {"$set": payload})

        if cursor is None:
            raise ValueError("User not found")

        return cursor
    except Exception as error:
        raise Exception("Erro: ", error)


# soft delete em um usuário com base no _id
def soft_delete_one(key):
    database = get_database()

    try:
        cursor = database.users.update_one({"_id": ObjectId(key)}, {"$set": {"is_active": False}})

        if cursor is None:
            raise ValueError("User not found")

        return cursor
    except Exception as error:
        raise Exception("Erro: ", error)


# Deleta um usuário com base no _id
def delete_one(key):
    database = get_database()

    try:
        cursor = database.users.delete_one({"_id": ObjectId(key)})

        if cursor is None:
            raise ValueError("User not found")

        return cursor
    except Exception as error:
        raise Exception("Erro: ", error)
