from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CosmosDBService:
    def __init__(self, connection_string, database_name, container_name):
        self.client = MongoClient(connection_string)
        self.database_name = database_name
        self.container_name = container_name
        self.database = self.client[database_name]
        self.container = self.database[container_name]

    def store_input(self, input_data):
        try:
            self.container.insert_one(input_data)
        except PyMongoError as e:
            print(f"An error occurred while storing data: {e}")

    def retrieve_input(self, item_id):
        try:
            return self.container.find_one({"_id": item_id})
        except PyMongoError as e:
            print(f"An error occurred while retrieving data: {e}")
            return None

    @staticmethod
    def init_cosmosdb(connection_string, database_name, container_name):
        client = MongoClient(connection_string)
        try:
            database = client[database_name]
            if container_name not in database.list_collection_names():
                database.create_collection(container_name)
            print(f"Database and container initialized: {database_name}/{container_name}")
            return CosmosDBService(connection_string, database_name, container_name)
        except PyMongoError as e:
            print(f"An error occurred during CosmosDB initialization: {e}")
            return None