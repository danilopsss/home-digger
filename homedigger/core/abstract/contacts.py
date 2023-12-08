from abc import ABC, abstractmethod


class ContactsABC(ABC):
    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def get_phone(self) -> str:
        ...

    @abstractmethod
    def get_email(self) -> str:
        ...
