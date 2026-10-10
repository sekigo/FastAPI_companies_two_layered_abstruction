from fastapi import APIRouter
from fastapi import HTTPException
from app.services import companies as company_service
from fastapi import status
from app.schemas import CompanyCreate, CompanyRead, CompanyUpdate
from app.database import SessionDep




router = APIRouter()


@router.get("/companies", status_code=200)
def list_companies(session: SessionDep)-> list[CompanyRead]:
    return company_service.list_companies(session)



@router.get("/companies/{company_id}", status_code=200)
def get_company(session: SessionDep, company_id: int)-> CompanyRead:
    try:
        company = company_service.get_company(session, company_id)
    except company_service.CompanyNotFoundError:
        raise HTTPException(status_code = 404, detail = "Company not found")
    return company




@router.post("/companies", status_code=201)
def create_company(session: SessionDep, data: CompanyCreate)-> CompanyRead:
    try:
        company = company_service.create_company(session, data)
    except company_service.CompanyConflictError:
        raise HTTPException(status_code=409, detail = "Company with this name already exists")
    return company




@router.delete("/companies/{company_id}", status_code=204)
def delete_companies(session: SessionDep, company_id: int)-> None:
    try:
        company_service.delete_company(session, company_id)
    except company_service.CompanyNotFoundError:
        raise HTTPException(status_code = 404, detail = "Company not found")





@router.patch("/companies/{company_id}", status_code=status.HTTP_200_OK)
def update_company(session: SessionDep,company_id: int, data: CompanyUpdate)-> CompanyRead:
    try:
        company = company_service.update_company(session,company_id, data)
    except company_service.CompanyNotFoundError:
        raise HTTPException(status_code = 404, detail = "Company not found")
    except company_service.CompanyConflictError:
        raise HTTPException(status_code=409, detail = "Company with this name already exists")
    return company
