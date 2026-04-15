from pydantic import BaseModel, ConfigDict
from schemas.person import Person

class TeacherCreate(BaseModel):
    person: Person
    academy: str | None = None

class Teacher(TeacherCreate):
    id: int

class TeacherUpdate(BaseModel):
    person: Person | None
    academy: str | None = None

model_config = ConfigDict(from_attributes=True)