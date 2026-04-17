from pydantic import BaseModel, ConfigDict

from schemas.person import PersonCreate


class TeacherResponse(BaseModel):
    id: int
    academy: str | None
    person: PersonCreate

model_config = ConfigDict(from_attributes=True)