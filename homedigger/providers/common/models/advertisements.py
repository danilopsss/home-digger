from sqlalchemy import Column, String, Integer, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import BaseModel
from .addresses import Addresses
from .contacts import Contacts


class Advertisements(BaseModel):
    __tablename__ = 'advertisements'

    price = Column(Integer, nullable=False, default=0)
    size = Column(Integer, nullable=False, default=0)
    bathrooms = Column(Integer, nullable=False, default=0)
    bedrooms = Column(Integer, nullable=False, default=0)
    has_lift = Column(Boolean, nullable=False, default=False)
    floor = Column(Integer, nullable=False, default=0)
    link = Column(String, nullable=False, default=None)

    address = relationship(Addresses, uselist=False, back_populates="advertisement")
    contact = relationship(Contacts, uselist=False, back_populates="advertisement")
    
    __tableargs__ = UniqueConstraint("link", name="unique_link")