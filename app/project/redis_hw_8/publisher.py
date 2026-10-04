from redis_hw_8.redis_client_hw import r
import time


for pub in range(0, 10):
    time.sleep(0.5)
    r.publish('python_channel', f'Hello Redis! Message #{pub}')