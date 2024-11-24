from src.database.tags import read, read_one


def handleTagsGet():
    """
    Escrever depois.
    """
    try:
        response = read()

        for tag in response:
            tag['_id'] = str(tag['_id'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")


def handleTagsGetOne(key):
    """
    Escrever depois.
    """
    try:
        response = read_one(key)

        response['_id'] = str(response['_id'])

        return response
    except Exception as error:
        raise Exception(f"Unexpected error: {error}")
