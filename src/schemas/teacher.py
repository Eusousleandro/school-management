from pydantic import BaseModel, ConfigDict

class TeacherCreate(BaseModel):
    name: str
    email: str
    cpf: str
    rg: str
    date_of_birth: str
    phone: str | None = None
    academy: str | None = None

class Teacher(TeacherCreate):
    id: int

class TeacherUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    cpf: str | None = None
    rg: str | None = None
    date_of_birth: str | None = None
    phone: str | None = None
    academy: str | None = None

model_config = ConfigDict(from_attributes=True)