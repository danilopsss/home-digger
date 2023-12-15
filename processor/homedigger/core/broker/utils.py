import os
import pika

from uuid import uuid4
from typing import Union
from homedigger.core.abstract.broker import BrokerAbstract


class Broker(BrokerAbstract):

    MessageBroker = Union[pika.BlockingConnection, None]

    def __init__(self):
        self.host = os.environ.get("BROKER_HOST", "broker")
        self.port = os.environ.get("BROKER_PORT", "5672")
        self.username = os.environ.get("BROKER_USERNAME", "RABBITMQ_DEFAULT_USER")
        self.password = os.environ.get("BROKER_PASSWORD", "RABBITMQ_DEFAULT_PASS")

    def get_broker_conn(self, broker: str) -> MessageBroker:
        brokers = {
            "rabbitmq": self.rabbitmq_connection
        }
        if broker not in brokers.keys():
            raise Exception("Broker not found")

        return brokers.get(broker)

    @property
    def rabbitmq_connection(self) -> pika.ConnectionParameters:
        credentials = pika.PlainCredentials(
            username=self.username,
            password=self.password
        ) 
        conn_params = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=credentials
        )
        return pika.BlockingConnection(conn_params)


def dispatch_message(function) -> dict:
    def dispatch(*args, **kwargs):
        message = function(*args, **kwargs)
        _broker = Broker()
        conn = _broker.get_broker_conn(message.get("broker"))

        with (channel := conn.channel()):
            channel.basic_publish(
                exchange=message.get("exchange", "file.created"),
                routing_key=message.get("routing_key", "file.created"),
                body=message.get("file", ""),
                properties=pika.BasicProperties(
                    message_id=str(uuid4()),
                )
            )
        message.pop("broker")
        return message
    return dispatch
