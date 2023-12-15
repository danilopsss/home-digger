import pika
from typing import Union, Any
from abc import ABC, abstractmethod



class BrokerAbstract(ABC):
    MessageBroker = Union[Any, Any]
    @abstractmethod
    def get_broker_conn(self, broker: str) -> dict: ...
    @property
    @abstractmethod
    def rabbitmq_connection(self) -> pika.ConnectionParameters: ...
