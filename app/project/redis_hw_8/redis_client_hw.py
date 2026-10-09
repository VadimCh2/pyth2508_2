import redis
import config_hw8

r = redis.Redis(
    host=config_hw8.REDIS_HOST,
    port=config_hw8.REDIS_PORT,
    decode_responses=True,
    username=config_hw8.REDIS_USERNAME,
    password=config_hw8.REDIS_PASSWORD,
)

# r.set('porshe gt3 rs','skorost')
# r.set('Alice','cat', ex=7200)
# r.rpush('products_list', "flour", "milk")
# r.expire('products_list',604800)
# r.hset('cake_ingredients', mapping={"flour": 250, "milk": 500})
# r.hset('cake_ingredients', "sugar", 300)
# r.hset('cake_ingredients', "sugar", 500)