__author__ = 'Svetleen'
import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()

    def insert(self, collection, data):
        Database.DATABASE["items"].insert({})