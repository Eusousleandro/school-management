from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(UserCreate):
    id: int

class UserUpdate(BaseModel):
    name: str | None
    email: str  | None
    password: str | None

model_config = ConfigDict(from_attributes=True)