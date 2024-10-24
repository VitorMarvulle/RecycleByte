from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def mongoDB():
    uri = "mongodb+srv://recycleadmin:garmKotmSHAwyGcg@cluster0.flsfq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri, server_api=ServerApi('1'))

    
    try:
        client.admin.command('ping')
        db=client.get_database('db_recycle')
        return db
    except Exception as e:
        print(e)

