from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from .base import BaseModel


class Addresses(BaseModel):
    __tablename__ = 'addresses'

    street = Column(String, nullable=False, default=None)   
    city = Column(String, nullable=False, default=None)

    advertisement_id = Column(UUID, ForeignKey("advertisements.id"))
    advertisement = relationship("Advertisements", lazy=True, uselist=False, back_populates="address")
