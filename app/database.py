from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from app.config import settings

if settings.database_url.startswith("sqlite"):
    engine = create_engine(settings.database_url, connect_args = {"check_same_thread": False})
else:
    engine = create_engine(settings.database_url)



class Base(DeclarativeBase):
    pass


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
