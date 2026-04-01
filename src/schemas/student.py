from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    photo: str
    name: str
    cpf: str
    rg: str
    address: str
    number: str
    complement: str
    city: str
    neighborhood: str
    state: str
    zip_code: str
    name_responsible_father: str
    name_responsible_mother: str
    academy_responsible: str
    financy_responsible: str
    email_responsible_acadamy: str
    financy_responsible_email: str
    phone_responsible_academy: str
    phone_responsible_financy: str

class Student(StudentCreate):
    id: int

class StudentUpdate(BaseModel):
    photo: str | None
    name: str | None
    cpf: str | None
    rg: str | None
    address: str | None
    number: str | None
    complement: str | None
    city: str | None
    neighborhood: str | None
    state: str | None
    zip_code: str | None
    name_responsible_father: str | None
    name_responsible_mother: str | None
    academy_responsible: str | None
    financy_responsible: str | None
    email_responsible_acadamy: str | None
    financy_responsible_email: str | None
    phone_responsible_academy: str | None
    phone_responsible_financy: str | None

model_config = ConfigDict(from_attributes=True)