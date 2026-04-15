from sqlalchemy import Column, String
from models.person import Person

class Student(Person):
    __tablename__ = "students"

    name_responsible_father = Column(String(255), nullable=True)
    name_responsible_mother = Column(String(255), nullable=True)
    academy_responsible = Column(String(255), nullable=True)
    financy_responsible = Column(String(255), nullable=True)
    email_responsible_acadamy = Column(String(255), nullable=True)
    financy_responsible_email = Column(String(255), nullable=True)
    phone_responsible_academy = Column(String(20), nullable=True)
    phone_responsible_financy = Column(String(20), nullable=True)
    photo = Column(String(255), nullable=True)