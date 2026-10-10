from app.models import Company
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas import CompanyCreate, CompanyUpdate

class CompanyNotFoundError(Exception):
    pass

class CompanyConflictError(Exception):
    pass


def list_companies(session: Session)-> list[Company]:
    return session.scalars(select(Company)).all()

def get_company(session: Session, company_id: int)-> Company:
    company = session.get(Company, company_id)
    if company is None:
        raise CompanyNotFoundError
    return company


def create_company(session: Session, data: CompanyCreate)-> Company:
    new_company = Company(**data.model_dump())
    session.add(new_company)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise CompanyConflictError

    session.refresh(new_company)
    return new_company



def delete_company(session: Session, company_id: int)-> None:
    company_exist = session.get(Company, company_id)
    if company_exist is None:
        raise CompanyNotFoundError
    session.delete(company_exist)
    session.commit()


def update_company(session: Session, company_id: int, data: CompanyUpdate)-> Company:
    updating_company = session.get(Company, company_id)
    if updating_company is None:
        raise CompanyNotFoundError

    updates = data.model_dump(exclude_unset = True)
    for key, val in updates.items():
        setattr(updating_company, key, val)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise CompanyConflictError
    session.refresh(updating_company)
    return updating_company
