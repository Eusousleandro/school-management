from datetime import date

from pydantic import BaseModel, EmailStr

class PersonBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    rg: str
    date_of_birth: date
    phone: str | None = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    cpf: str | None = None
    rg: str | None = None
    date_of_birth: date | None = None
    address: str | None = None
    number: str | None = None
    complement: str | None = None
    city: str | None = None
    neighborhood: str | None = None
    state: str | None = None
    zip_code: str | None = None
    phone: str | None = None