from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.datasource.database import Base

class Client(Base):
    __tablename__   = "tb_clients"

    id              = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    name            = Column(String, nullable = False)
    phone           = Column(String, nullable = False)
    address         = Column(String, nullable = False)
    address_number  = Column(Integer, nullable = False)

    orders = relationship('Order', back_populates = 'client')

class Order(Base):
    __tablename__   = 'tb_orders'

    id              = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    product_name    = Column(String, nullable = False)
   
    client_id       = Column(UUID(as_uuid=True), ForeignKey("tb_clients.id"))
    client          = relationship("Client", back_populates = "orders")