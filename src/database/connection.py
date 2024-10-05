import dotenv
import os

from pymongo import MongoClient

dotenv.load_dotenv()

uri = os.getenv('CONNECTION_URI')
client = MongoClient(uri)


def get_connection():
    try:
        database = client.get_database("test")
        data = database.get_collection("data")

        query = {"title": "Just a test"}
        results = data.find_one(query)

        print(results)

        client.close()

    except Exception as error:
        raise Exception("Não encontrado por: ", error)
