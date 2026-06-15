from redis_client import redis_client

redis_client.lpush("tasks", "send_email")
redis_client.lpush("tasks", "generate_invoice")

print(redis_client.lrange("tasks", 0, -1))

task = redis_client.rpop("tasks")
print(task)

print(redis_client.lrange("tasks", 0, -1))