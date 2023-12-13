from homedigger.providers.common.schemas.base import Base
from homedigger.providers.common.models.advertisements import Advertisements
from homedigger.providers.common.schemas.addresses import AddressSchema
from homedigger.providers.common.schemas.contacts import ContactsSchema


class IdealistaSchema(Base):
    __orm_model__ = Advertisements

    price: int
    size: int
    bathrooms: int
    bedrooms: int
    has_lift: bool
    floor: int
    link: str

    address: AddressSchema
    contact: ContactsSchema
