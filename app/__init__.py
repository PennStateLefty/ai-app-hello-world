from flask import Flask
from .services.cosmosdb import init_cosmosdb
from .services.redis_cache import init_redis_cache

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Initialize CosmosDB
    init_cosmosdb(app)

    # Initialize Redis Cache
    init_redis_cache(app)

    from . import routes

    return app