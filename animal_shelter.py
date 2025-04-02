from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB"""

    def __init__(self):
        # MongoDB connection setup
        USER = 'aacuser'
        PASS = 'Test1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31930
        DB = 'AAC'
        COL = 'animals'
        
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
            self.database = self.client[DB]
            self.collection = self.database[COL]
        except PyMongoError as e:
            print("Connection error:", e)
            raise

    def create(self, data):
        """Insert a document into the collection"""
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged  # True if success
            except PyMongoError as e:
                print("Insert error:", e)
                return False
        else:
            raise ValueError("No data provided to insert.")

    def read(self, query):
        """Find documents using the query"""
        try:
            cursor = self.collection.find(query)
            return list(cursor)  # Return results as list
        except PyMongoError as e:
            print("Read error:", e)
            return []
        
    def update_documents(self, query, new_values):
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    def delete_documents(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0
