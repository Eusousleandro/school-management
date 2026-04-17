from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str | None
    email: str  | None
    password: str | None

model_config = ConfigDict(from_attributes=True)