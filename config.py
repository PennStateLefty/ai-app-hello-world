import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    COSMOSDB_CONNECTION_STRING = os.environ.get('COSMOSDB_CONNECTION_STRING')
    COSMOSDB_KEY = os.environ.get('COSMOSDB_KEY')
    COSMOSDB_DATABASE_NAME = os.environ.get('COSMOSDB_DATABASE_NAME')
    COSMOSDB_CONTAINER_NAME = os.environ.get('COSMOSDB_CONTAINER_NAME')
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    AZURE_OPENAI_API_KEY = os.environ.get('AZURE_OPENAI_API_KEY')
    AZURE_OPENAI_ENDPOINT = os.environ.get('AZURE_OPENAI_ENDPOINT') or 'https://your-openai-endpoint.azure.com/'