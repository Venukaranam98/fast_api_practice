from redis_client import redis_client

redis_client.set("name", "Venu")

print(redis_client.get("name"))