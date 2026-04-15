from pydantic import BaseModel, ConfigDict
from schemas.person import Person

class TeacherBase(BaseModel):
    person: Person | None = None
    academy: str | None = None

class TeacherCreate(TeacherBase):
    person: Person

class TeacherUpdate(TeacherBase):
    person: Person | None
    academy: str | None = None

class TeacherResponse(TeacherBase):
    id: int
    person: Person

model_config = ConfigDict(from_attributes=True)