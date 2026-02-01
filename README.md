# CRUD Pizzaria API

API REST para cadastro de clientes e pedidos de uma pizzaria.

## Tecnologias
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Estrutura
app/
├── src/
│   ├── datasource/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── deps.py
│   │   ├── schemas.py
│   │   ├── create_tables.py
│   │   └── pizzaria.db
│   ├── routes.py
│   └── main.py
└── tests/

## Modelagem
- Cliente (tb_clients)
- Pedido (tb_orders)
- Relacionamento 1:N (cliente → pedidos)

## Banco de dados
- SQLite
- Banco local (`pizzaria.db`)
- Criação via SQLAlchemy ORM

## Como executar

### 1. Instalar dependências
```bash
python -m pip install fastapi uvicorn sqlalchemy
```
### 2. Criar tabelas
```bash
cd app
python -m src.datasource.create_tables
```
### 3. Subir a API
```bash
python -m uvicorn src.main:app --reload
```
### EXTRA - Acessar a docs 
```bash
http://localhost:8000/docs
```

## O que está pronto:
 - CRUD parcial de clientes e pedidos
 - Banco funcional
 - Estrutura organizada

## Próximos passos:
 Os próximos passos são implementar o CRUD completo de pedidos e orders (filtros por cliente, etc), adicionar os métodos PUT e DELETE para clientes e pedidos, criar testes automatizados