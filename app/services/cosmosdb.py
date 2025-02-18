from azure.cosmos import CosmosClient, exceptions

class CosmosDBService:
    def __init__(self, endpoint, key, database_name, container_name):
        self.client = CosmosClient(endpoint, key)
        self.database_name = database_name
        self.container_name = container_name
        self.database = self.client.get_database_client(database_name)
        self.container = self.database.get_container_client(container_name)

    def store_input(self, input_data):
        try:
            self.container.create_item(input_data)
        except exceptions.CosmosHttpResponseError as e:
            print(f"An error occurred while storing data: {e}")

    def retrieve_input(self, item_id):
        try:
            return self.container.read_item(item=item_id, partition_key=item_id)
        except exceptions.CosmosHttpResponseError as e:
            print(f"An error occurred while retrieving data: {e}")
            return None