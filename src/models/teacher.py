from sqlalchemy import Column, Integer, String
from models.person import Person

class Teacher(Person):
    __tablename__ = 'teachers'

    academy = Column(String(255), nullable=True)
    discipline = Column(String(255), nullable=True)

