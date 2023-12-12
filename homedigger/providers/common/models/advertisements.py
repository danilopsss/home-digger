from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, UniqueConstraint
from .base import BaseModel


class Advertisements(BaseModel):
    __tablename__ = 'advertisements'
    __tableargs__ = UniqueConstraint("link", name="unique_link")

    price = Column(Integer, nullable=False, default=0)
    size = Column(Integer, nullable=False, default=0)
    bathrooms = Column(Integer, nullable=False, default=0)
    bedrooms = Column(Integer, nullable=False, default=0)
    has_lift = Column(Boolean, nullable=False, default=False)
    floor = Column(Integer, nullable=False, default=0)
    link = Column(String, nullable=False, default=None)

    address = relationship("Addresses", lazy=True, uselist=False, back_populates="advertisement")
    contact = relationship("Contacts", lazy=True, uselist=False, back_populates="advertisement")
