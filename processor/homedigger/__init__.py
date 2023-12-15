
from pathlib import Path
from homedigger.core.scrapper import Scrapper
from homedigger.core.broker.utils import Broker


def process_incoming_data(*args) -> None:
    _, _, _, message = args
    path = message.decode("utf-8")
    if path:
        filepath = Path("/tmp/html").joinpath(path).resolve()
        data = Scrapper(filepath=filepath).run()
        data.save()


def consume_from_queue(broker: str, queue: str) -> dict:
    _broker = Broker()
    conn = _broker.get_broker_conn(broker)
    channel = conn.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_qos(prefetch_count=3)
    channel.queue_bind(queue, exchange=queue, routing_key=queue)
    channel.basic_consume(queue, process_incoming_data, auto_ack=True)
    channel.start_consuming()

def run():
    consume_from_queue("rabbitmq", "file.created")