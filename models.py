from sqlalchemy import Column, String, Integer 
from database import Base

class Student(Base): 
    __tablename__ = "students" 
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String(50), nullable=False) 