from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.datasource.models import Client, Order
from src.datasource.schemas import CreateClient, CreateOrder
from src.datasource.deps import get_db

router = APIRouter()

@router.get('/')
async def root():
    return ("Bem vindo a nossa pizzaria!!!", {"Horário de funcionamento:": "13h às 22h"})

@router.post('/clients', status_code=201)
async def create_client(data: CreateClient, db: Session = Depends(get_db)):
    client  = Client(**data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.get('/clients')
async def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.post('/orders', status_code=201)
async def create_order(data: CreateOrder, db: Session = Depends(get_db)):
    order   = Order(
        product_name = data.product_name,
        client_id    = data.client_id
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get('/orders')
async def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()