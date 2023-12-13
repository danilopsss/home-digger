from .base import Base
from homedigger.providers.common.models.addresses import Addresses


class AddressSchema(Base):
    __orm_model__ = Addresses

    street: str
    city: str
