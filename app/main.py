from fastapi import FastAPI
from controller.routes import router
from model.database import engine, Base
from model import models

##Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)