import redis
import time

# Connect to Redis
r = redis.Redis()

# Test uncached access
start = time.time()
r.get("uncached_data")  # Key doesn't exist
uncached_time = time.time() - start

# Test cached access
r.set("cached_data", "Hello from cache!")
start = time.time()
r.get("cached_data")  # Key exists in memory
cached_time = time.time() - start

# Print results
print(f"Uncached: {uncached_time:.5f} sec")
print(f"Cached: {cached_time:.5f} sec  # {int(uncached_time/cached_time)}x faster!")