import os
import dotenv
from flask import g
from pymongo import MongoClient

dotenv.load_dotenv()

uri = os.getenv('CONNECTION_URI')


def get_client():
    if "db_client" not in g:
        g.db_client = MongoClient(uri)
    return g.db_client


def get_database():
    client = get_client()
    return client["cafe_reparo"]
