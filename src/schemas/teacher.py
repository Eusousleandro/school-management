from pydantic import BaseModel, ConfigDict
from schemas.person import PersonCreate, PersonUpdate

class TeacherBase(BaseModel):
    academy: str | None = None

class TeacherCreate(TeacherBase):
    person: PersonCreate

class TeacherUpdate(BaseModel):
    academy: str | None = None
    person: PersonUpdate | None = None

model_config = ConfigDict(from_attributes=True)