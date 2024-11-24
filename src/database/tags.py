from bson import ObjectId
from pymongo.errors import PyMongoError

from src.database.connection import get_database


def read():
    """
    Escrever depois.
    """
    database = get_database()

    try:
        cursor = database.tags.find({})

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
        cursor = database.tags.find_one({'_id': ObjectId(key)})

        if cursor is None:
            raise ValueError("Cursor not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")
