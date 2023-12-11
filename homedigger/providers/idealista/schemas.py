from pydantic import BaseModel
from homedigger.providers.common.schemas.contacts import ContactsSchema
from homedigger.providers.common.schemas.addresses import AddressSchema


class IdealistaSchema(BaseModel):
    price: int
    size: int
    bathrooms: int
    bedrooms: int
    has_lift: bool
    floor: int
    link: str

    address: AddressSchema
    contact: ContactsSchema
