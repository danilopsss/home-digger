from pydantic import Field
from .base import Base
from homedigger.providers.common.models.contacts import Contacts


class ContactsSchema(Base):
    __orm_model__ = Contacts

    name: str
    city: str
    phone: str = Field(default="")
    email: str = Field(default="")
