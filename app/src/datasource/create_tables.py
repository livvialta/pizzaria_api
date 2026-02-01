from src.datasource.database import engine, Base
import src.datasource.models

Base.metadata.create_all(bind=engine)