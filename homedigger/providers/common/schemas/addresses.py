from pydantic import BaseModel


class AddressSchema(BaseModel):
    street: str
    city: str
