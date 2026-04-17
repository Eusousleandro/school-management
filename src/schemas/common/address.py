from pydantic import BaseModel

class AddressBase(BaseModel):
    address: str
    number: str
    complement: str | None = None
    city: str
    neighborhood: str
    state: str
    zip_code: str

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    address: str | None = None
    number: str | None = None
    complement: str | None = None
    city: str | None = None
    neighborhood: str | None = None
    state: str | None = None
    zip_code: str | None = None