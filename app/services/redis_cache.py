from redis import Redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = Redis(host=host, port=port, db=db)

    def set_cache(self, key, value, expiration=None):
        self.redis_client.set(key, json.dumps(value), ex=expiration)

    def get_cache(self, key):
        value = self.redis_client.get(key)
        return json.loads(value) if value else None

    def delete_cache(self, key):
        self.redis_client.delete(key)