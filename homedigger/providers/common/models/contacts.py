from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from .base import BaseModel


class Contacts(BaseModel):
    __tablename__ = 'contacts'

    name = Column(String, nullable=False, default="")
    city = Column(String, nullable=False, default="")
    phone = Column(String, nullable=True, default=None)
    email = Column(String, nullable=True, default=None)

    advertisement_id = mapped_column(ForeignKey('advertisements.id'))
    advertisements = relationship('Advertisements', back_populates='contacts')
