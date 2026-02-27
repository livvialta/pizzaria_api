from pydantic import BaseModel
from uuid import UUID

class CreateClient(BaseModel):
    name: str
    phone: str
    address: str
    address_number: int

class CreateOrder(BaseModel):
    product_id: UUID
    client_id: UUID

class CreateProduct(BaseModel):
    product_name: str
    price: float
