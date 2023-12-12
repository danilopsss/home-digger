from abc import ABC, abstractmethod
from homedigger.providers.common.types.providers import Provider
from homedigger.providers.common.schemas.contacts import ContactsSchema


class ProvidersInformationABC(ABC):
    @property
    @abstractmethod
    def _scrapper_rules(self) -> tuple: ...
    @property
    @abstractmethod
    def get_price(self) -> int: ...
    @property
    @abstractmethod
    def _get_details(self) -> list: ...
    @property
    @abstractmethod
    def get_size(self) -> int: ...
    @property
    @abstractmethod
    def get_floor(self) -> int: ...
    @property
    @abstractmethod
    def has_lift(self) -> bool: ...
    @property
    @abstractmethod
    def get_bedrooms_number(self) -> int: ...
    @property
    @abstractmethod
    def get_bathrooms_number(self) -> int: ...
    @property
    @abstractmethod
    def get_contacts(self) -> ContactsSchema: ...
    @property
    @abstractmethod
    def get_address_dict(self) -> dict: ...
    @property
    @abstractmethod
    def get_data(self) -> Provider: ...
    @property
    @abstractmethod
    def get_link(self) -> Provider: ...
    @property
    @abstractmethod
    def get_soup(self) -> str: ...
