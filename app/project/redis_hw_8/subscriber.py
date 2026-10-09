from redis_hw_8.redis_client_hw import r

subscriber = r.pubsub()
subscriber.subscribe('python_channel')

for message in subscriber.listen():
    print(message)