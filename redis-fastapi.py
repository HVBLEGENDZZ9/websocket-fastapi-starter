import redis
from fastapi import FastAPI

app = FastAPI()

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cached_item = redis_client.get(f"item_{item_id}")
    
    if cached_item:
        return {"item_id": item_id, "cached": True, "data": cached_item.decode('utf-8')}
    
    # Simulate data fetching process
    item_data = f"Item data for {item_id}"
    
    # Store the item in Redis for future requests
    redis_client.set(f"item_{item_id}", item_data)
    
    return {"item_id": item_id, "cached": False, "data": item_data}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cached_item = redis_client.get(f"item_{item_id}")
    
    if cached_item:
        return {"item_id": item_id, "cached": True, "data": cached_item.decode('utf-8')}
    
    item_data = f"Item data for {item_id}"
    
    # Store the item in Redis with an expiration time of 1 hour (3600 seconds)
    redis_client.setex(f"item_{item_id}", 3600, item_data)
    
    return {"item_id": item_id, "cached": False, "data": item_data}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    redis_client.delete(f"item_{item_id}")
    return {"status": "cache cleared"}
