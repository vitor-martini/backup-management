from http import client
from pymongo import MongoClient
import services.database as bd

def adicionar(arquivo, caminho):
    dbname = bd.get_database()
    collection_name = dbname["arquivos"]

    item_1 = {
    "arquivo" : arquivo,
    "caminho" : caminho
    }

    collection_name.insert_one(item_1)