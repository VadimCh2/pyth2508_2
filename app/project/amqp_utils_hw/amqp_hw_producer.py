from pika.adapters import blocking_connection
from amqp_utils_hw.amqp_hw_client import get_connection
import time


def produce_message(channel: blocking_connection.BlockingConnection) -> None:
    QUEUE = 'weather'
    channel.queue_declare(QUEUE)

    message = 'Chernyakov Vadym {item}'
    for item in range(221):
        time.sleep(0.1)
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message.format(item=item)
        )
        print(item)


def main_producer():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel)