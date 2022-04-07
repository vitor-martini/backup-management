from http import client
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://sa:21081999@backup-management.cocs7.mongodb.net/backup-management-bd"
    client = MongoClient(CONNECTION_STRING)
    return client['backup-management-bd']

if __name__ == "__main__":
    dbname = get_database()
