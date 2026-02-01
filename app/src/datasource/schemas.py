from pydantic import BaseModel
from uuid import UUID

class CreateClient(BaseModel):
    name: str
    phone: str
    address: str
    address_number: int

class ResponseClient(CreateClient):
    id: UUID

class CreateOrder(BaseModel):
    product_name: str
    client_id: str