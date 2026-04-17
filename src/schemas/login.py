from pydantic import BaseModel, Field

class Login(BaseModel):
    email: str
    password: str = Field(max_length=72)