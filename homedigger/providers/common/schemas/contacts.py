from pydantic import BaseModel, Field
from typing import Optional


class ContactsSchema(BaseModel):
    name: str
    city: str
    phone: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
