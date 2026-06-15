from redis_client import redis_client
import time

redis_client.set("otp", "123456", ex=10)

print(redis_client.get("otp"))
print(redis_client.ttl("otp"))

time.sleep(12)

print(redis_client.get("otp"))