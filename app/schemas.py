from pydantic import BaseModel, ConfigDict




class CompanyRead(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    name: str
    industry: str


class CompanyCreate(BaseModel):
    name: str
    industry: str


class CompanyUpdate(BaseModel):
    name: str | None = None
    industry: str | None = None
