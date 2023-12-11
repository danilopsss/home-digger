from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from .base import BaseModel


class Addresses(BaseModel):
    __tablename__ = 'addresses'

    street = Column(String, nullable=False, default=None)   
    city = Column(String, nullable=False, default=None)
    
    advertisement_id = mapped_column(ForeignKey('advertisements.id'))
    advertisements = relationship('Advertisements', back_populates='address')
