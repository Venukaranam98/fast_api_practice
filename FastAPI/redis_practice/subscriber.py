import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

pubsub = redis_client.pubsub()

pubsub.subscribe("orders")

print("Waiting for messages...")

for message in pubsub.listen():
    if message["type"] == "message":
        print(message["data"])