from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    id: int
    email: str  | None
    password: str | None

model_config = ConfigDict(from_attributes=True)