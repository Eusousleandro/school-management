from pydantic import BaseModel, ConfigDict

from schemas.person import PersonCreate


class StudentResponse(BaseModel):
    id: int
    person: PersonCreate
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