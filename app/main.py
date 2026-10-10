from fastapi import FastAPI
from app.database import Base, engine
from app.routers import companies


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(companies.router)
