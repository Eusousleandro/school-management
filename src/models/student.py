from sqlalchemy import Column, Integer, String
from config.database.session import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    rg = Column(String(20), unique=True, index=True, nullable=False)
    date_of_birth = Column(String(10), nullable=False)
    address = Column(String(255), nullable=False)
    number = Column(String(10), nullable=False)
    complement = Column(String(255), nullable=True)
    city = Column(String(255), nullable=False)
    neighborhood = Column(String(255), nullable=False)
    state = Column(String(2), nullable=False)
    zip_code = Column(String(10), nullable=False)
    phone = Column(String(20), nullable=True);
    name_responsible_father = Column(String(255), nullable=True)
    name_responsible_mother = Column(String(255), nullable=True)
    academy_responsible = Column(String(255), nullable=True)
    financy_responsible = Column(String(255), nullable=True)
    email_responsible_acadamy = Column(String(255), nullable=True)
    financy_responsible_email = Column(String(255), nullable=True)
    phone_responsible_academy = Column(String(20), nullable=True)
    phone_responsible_financy = Column(String(20), nullable=True)
    photo = Column(String(255), nullable=True)