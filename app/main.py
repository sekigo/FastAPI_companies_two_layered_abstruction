from fastapi import FastAPI
from app.routers import companies



app = FastAPI()
app.include_router(companies.router)
