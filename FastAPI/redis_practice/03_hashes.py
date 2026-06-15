from redis_client import redis_client

redis_client.hset(
    "user:1",
    mapping={
        "name": "Venu",
        "email": "venu@example.com",
        "age": 22
    }
)

print(redis_client.hgetall("user:1"))
print(redis_client.hget("user:1", "name"))