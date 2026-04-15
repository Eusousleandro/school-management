from pydantic import BaseModel
class Person(BaseModel):
    name: str
    cpf: str
    rg: str
    address: str
    number: str
    complement: str
    city: str
    neighborhood: str
    state: str
    zip_code: str