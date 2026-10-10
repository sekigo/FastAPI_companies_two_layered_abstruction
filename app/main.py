from fastapi import FastAPI
from sqlalchemy import String, select
from app.database import Base, engine
from app.routers import companies


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(companies.router)
