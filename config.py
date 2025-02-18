import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    COSMOSDB_CONNECTION_STRING = os.environ.get('COSMOSDB_CONNECTION_STRING')
    REDIS_URL = os.environ.get('REDIS_URL')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_ENDPOINT = os.environ.get('OPENAI_ENDPOINT') or 'https://your-openai-endpoint.azure.com/'