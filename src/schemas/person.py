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

class PersonUpdate(Person):
    name: str | None
    cpf: str | None
    rg: str | None
    address: str | None
    number: str | None
    complement: str | None
    city: str | None
    neighborhood: str | None
    state: str | None
    zip_code: str | None