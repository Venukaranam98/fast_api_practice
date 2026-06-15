from redis_client import redis_client
import time
import json


def get_product_from_db(product_id):
    print("Fetching from database...")
    time.sleep(3)

    return {
        "id": product_id,
        "name": "iPhone 16",
        "price": 99999
    }


def get_product(product_id):
    cache_key = f"product:{product_id}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Cache hit!")

        return json.loads(cached_data)

    print("Cache miss!")

    product = get_product_from_db(product_id)

    redis_client.set(
        cache_key,
        json.dumps(product),
        ex=60
    )

    return product


print(get_product(101))
print(get_product(101))