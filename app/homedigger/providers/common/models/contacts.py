from sqlalchemy.orm import  relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from .base import BaseModel


class Contacts(BaseModel):
    __tablename__ = 'contacts'

    name = Column(String, nullable=False, default="")
    city = Column(String, nullable=False, default="")
    phone = Column(String, nullable=True, default=None)
    email = Column(String, nullable=True, default=None)

    advertisement_id = Column(UUID, ForeignKey("advertisements.id"), nullable=False)
    advertisement = relationship("Advertisements", lazy=True, uselist=False, back_populates="contact")
