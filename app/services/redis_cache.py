from redis import Redis
import json
import re
import redis

# class RedisCache:
#     def __init__(self, connection_string):
#         self.redis_client = Redis.from_url(self._parse_redis_url(connection_string))

#     def _parse_redis_url(self, connection_string):
#         match = re.match(r'([^:]+):(\d+),password=([^,]+),ssl=True,abortConnect=False', connection_string)
#         if not match:
#             raise ValueError("Invalid Azure Redis connection string format")
#         host, port, password = match.groups()
#         return f"rediss://:{password}@{host}:{port}/0"

#     def set_cache(self, key, value, expiration=None):
#         self.redis_client.set(key, json.dumps(value), ex=expiration)

#     def get_cache(self, key):
#         value = self.redis_client.get(key)
#         return json.loads(value) if value else None

#     def delete_cache(self, key):
#         self.redis_client.delete(key)

class RedisCacheService:
    def __init__(self, host, port, password):
        self.client = redis.StrictRedis(host=host, port=port, password=password, ssl=True, decode_responses=True)

    def store_result(self, key, value):
        self.client.set(key, value)

    def get_cache(self, key):
        value = self.redis_client.get(key)
        return json.loads(value) if value else None

    @staticmethod
    def init_redis_cache(host, port, password):
        try:
            redis_service = RedisCacheService(host, port, password)
            print(f"Redis cache initialized: {host}:{port}")
            print("Testing the connection...")
            redis_service.client.ping()  # Test the connection
            return redis_service
        except Exception as e:
            print(f"An error occurred during Redis cache initialization: {e}")
            return None

# def init_redis_cache(connection_string):
#     try:
#         redis_client = Redis.from_url(RedisCache._parse_redis_url(None, connection_string))
#         # Test the connection
#         redis_client.ping()
#         print(f"Redis cache initialized with connection string: {connection_string}")
#         return redis_client
#     except Exception as e:
#         print(f"An error occurred during Redis cache initialization: {e}")
#         return None