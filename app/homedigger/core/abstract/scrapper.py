from abc import ABC, abstractmethod
from homedigger.providers.common.types.providers import Provider


class ScrapperABC(ABC):
    @abstractmethod
    def __init__(self, filepath: str) -> None: ...
    @property
    @abstractmethod
    def get_raw_file(self) -> str: ...
    @property
    @abstractmethod
    def get_providers(self) -> dict[str, Provider]: ...
