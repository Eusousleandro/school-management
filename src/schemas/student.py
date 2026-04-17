from pydantic import BaseModel, ConfigDict
from schemas.person import PersonCreate, PersonUpdate

class StudentBase(BaseModel):
    photo: str | None = None
    name_responsible_father: str | None = None
    name_responsible_mother: str | None = None
    academy_responsible: str | None = None
    financy_responsible: str | None = None
    email_responsible_acadamy: str | None = None
    financy_responsible_email: str | None = None
    phone_responsible_academy: str | None = None
    phone_responsible_financy: str | None = None

class StudentCreate(StudentBase):
    person: PersonCreate

class StudentUpdate(BaseModel):
    person: PersonUpdate | None = None
    photo: str | None = None
    name_responsible_father: str | None = None
    name_responsible_mother: str | None = None
    academy_responsible: str | None = None
    financy_responsible: str | None = None
    email_responsible_acadamy: str | None = None
    financy_responsible_email: str | None = None
    phone_responsible_academy: str | None = None
    phone_responsible_financy: str | None = None

model_config = ConfigDict(from_attributes=True)