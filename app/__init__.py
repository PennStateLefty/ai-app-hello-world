from flask import Flask
from .services.cosmosdb import CosmosDBService
from .services.redis_cache import RedisCacheService
from .routes import bp as main_bp

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Initialize CosmosDB
    app.cosmosdb_service = CosmosDBService.init_cosmosdb(
        connection_string=app.config['COSMOSDB_CONNECTION_STRING'],
        database_name=app.config['COSMOSDB_DATABASE_NAME'],
        container_name=app.config['COSMOSDB_CONTAINER_NAME']
    )

    # Initialize Redis Cache
    app.redis_cache_service = RedisCacheService.init_redis_cache(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        password=app.config['REDIS_PASSWORD']
    )

    # Register blueprint
    app.register_blueprint(main_bp)

    return app