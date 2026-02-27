from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model.models import Client, Order, Catalog
from schema.schemas import CreateClient, CreateOrder, CreateProduct
from core.deps import get_db
from uuid import UUID

router = APIRouter()

##COMO SEPARAR REGRA DE NEGOCIO DE ROTAS? PERGUNTAR PRA MARI.

@router.get('/')
async def root():
    return ("Bem vindo a nossa pizzaria!!!", {"Horário de funcionamento:": "13h às 22h"})

#CLIENTS
@router.post('/create_clients', status_code=201)
async def create_client(data: CreateClient, db: Session = Depends(get_db)):
    client  = Client(**data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.get('/clients')
async def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.get('/client/{id}')
async def get_client(id: UUID, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put('/update_client/{client_id}')
async def update_client(client_id: UUID, data: CreateClient, db: Session = Depends(get_db)):

    client = db.query(Client).filter(Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code = 404, detail='Client not found')
    
    client.name             = data.name
    client.phone            = data.phone
    client.address          = data.address
    client.address_number   = data.address_number

    db.commit()
    db.refresh(client)
    return client

#ORDERS
@router.post('/create_orders', status_code=201)
async def create_order(data: CreateOrder, db: Session = Depends(get_db)):

    catalog = db.query(Catalog).filter(Catalog.id == data.product_id).first()

    if not catalog:
        raise HTTPException(status_code =404, detail="Product not found")
         
    order   = Order(
        product_id = data.product_id,
        client_id    = data.client_id
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get('/orders')
async def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get('/order/{id}')
async def list_order(id: UUID, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Catalog.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order

#CATALOG
@router.post('/create_catalog_product', status_code=201)
async def create_catalog_product(data: CreateProduct, db: Session = Depends(get_db)):
    product = Catalog(
        product_name    = data.product_name,
        price           = data.price
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.put('/update_catalog_product/{product_id}')
async def update_catalog_product(product_id: UUID, data: CreateProduct, db: Session = Depends(get_db)):
    
    product = db.query(Catalog).filter(Catalog.id == product_id).first()

    if not product:
        raise HTTPException(status_code =404, detail='Product not found')
    
    product.product_name    = data.product_name
    product.price           = data.price
    
    db.commit()
    db.refresh(product)
    return product

@router.get('/catalog')
async def list_catalog(db: Session = Depends(get_db)):
    return db.query(Catalog).all()

@router.get('/catalog/{id}')
async def list_catalog(id: UUID, db: Session = Depends(get_db)):
    item = db.query(Catalog).filter(Catalog.id == id).first()

    if not item:
        raise HTTPException(status_code = 404, detail='Item not found')
    return item