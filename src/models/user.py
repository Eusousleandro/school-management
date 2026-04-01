from sqlalchemy import Column, Integer, String
from config.database.session import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    password = Column(String(250), nullable=False)