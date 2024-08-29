
from pymongo import MongoClient

class Mongo:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri
        self.connection = MongoClient(mongo_uri)
    
    def get_connection(self) -> MongoClient:
        return self.connection