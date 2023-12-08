from typing import Union
from abc import ABC, abstractmethod
from homedigger.providers.common.types import Provider, DataDict


class SanitizationABC(ABC):
    @staticmethod
    @abstractmethod
    def clean_up_integer(value: Union[str, int]) -> int:
        ...

    @staticmethod
    @abstractmethod
    def clean_up_text(value: str) -> str:
        ...

    @staticmethod
    @abstractmethod
    def clean_up_by_schema(data: DataDict, model: Provider) -> Provider:
        ...
