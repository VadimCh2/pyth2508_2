import redis
import config

r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

# r.set('porshe gt3 rs','skorost')
# r.set('Alice','cat', ex=7200)
# r.rpush('products_list', "flour", "milk")
# r.expire('products_list',604800)
# r.hset('cake_ingredients', mapping={"flour": 250, "milk": 500})
# r.hset('cake_ingredients', "sugar", 300)
# r.hset('cake_ingredients', "sugar", 500)