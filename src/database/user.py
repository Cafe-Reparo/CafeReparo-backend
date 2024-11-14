from bson import ObjectId
from pymongo.errors import PyMongoError
from src.database.connection import get_database


def create(payload):
    """
    Cria um usuário no banco de dados.
    Insere os dados no banco de dados e armazena a resposta.
    Retorna a resposta do banco de dados, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.insert_one(payload)

        if cursor is None:
            raise ValueError("Not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def read():
    """
    Busca todos os usuários do banco de dados.
    Filtra por usuários marcados como ativos, ignora campos sensíveis.
    Retorna uma lista com todos os usuários ativos, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.find({'is_active': True}, {'picture': 0, 'is_active': 0, 'password': 0})

        if cursor is None:
            raise ValueError("Cursor not found")

        return list(cursor)
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def read_one(key):
    """
    Busca um usuário do banco de dados com base em um parâmetro.
    Filtra por usuários marcados como ativos, ignora campos sensíveis.
    Retorna o usuário encontrado, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.find_one({'_id': ObjectId(key), 'is_active': True}, {'picture': 0, 'is_active': 0, 'password': 0})

        if cursor is None:
            raise ValueError("Cursor not found")

        return cursor
    except PyMongoError as db_error:
        raise Exception(f"Database error occurred: {db_error}")


def update_one(key, payload):
    """
    Atualiza um usuário no banco de dados com base em um parâmetro.
    Substitui o usuário com os dados passados no corpo da requisição.
    Retorna a resposta da operação recebida do banco de dados, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.update_one({'_id': ObjectId(key)}, {'$set': payload})

        if cursor is None:
            raise ValueError('User not found')

        return cursor
    except PyMongoError as db_error:
        raise Exception(f'Database error occurred: {db_error}')


def soft_delete_one(key):
    """
    Marca o usuário para ser ignorado em qualquer operação futura.
    Altera o campo is_active do _id encontrado para false.
    Retorna uma mensagem de sucesso e o _id do usuário atualizado, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.update_one({'_id': ObjectId(key)}, {'$set': {'is_active': False}})

        if cursor is None:
            raise ValueError('User not found')

        return cursor
    except PyMongoError as db_error:
        raise Exception(f'Database error occurred: {db_error}')


def delete_one(key):
    """
    Remove o usuário do banco de dados com base no _id.
    NÃO DEVERÁ SER UTILIZADO SEM NECESSIDADE EXPLÍCITA.
    Retorna uma mensagem de sucesso e o _id do usuário removido, ou erro.
    """
    database = get_database()

    try:
        cursor = database.users.delete_one({'_id': ObjectId(key)})

        if cursor is None:
            raise ValueError('User not found')

        return cursor
    except PyMongoError as db_error:
        raise Exception(f'Database error occurred: {db_error}')
