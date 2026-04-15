from pydantic import BaseModel, ConfigDict
from schemas.person import Person, PersonUpdate

class StudentBase(BaseModel):
    person: Person | None
    photo: str | None
    name_responsible_father: str | None
    name_responsible_mother: str | None
    academy_responsible: str | None
    financy_responsible: str | None
    email_responsible_acadamy: str | None
    financy_responsible_email: str | None
    phone_responsible_academy: str | None
    phone_responsible_financy: str | None

class StudentCreate(StudentBase):
    person: Person

class StudentUpdate(StudentBase):
    person: PersonUpdate | None

class StudentResponse(StudentBase):
    id: int
    person: Person

model_config = ConfigDict(from_attributes=True)