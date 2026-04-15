from pydantic import BaseModel, ConfigDict
from schemas.person import Person

class StudentCreate(BaseModel):
    person: Person
    photo: str
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

model_config = ConfigDict(from_attributes=True)