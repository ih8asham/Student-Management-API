from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = "root"
DB_PASSWORD = "71102" 
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "student_db"

DATABASE_URL = ("mysql+pymysql://root:71102@localhost:3306/student_db")

engine = create_engine(DATABASE_URL) 

SessionLocal = sessionmaker (
    autocommit = False,
    autoflush = False,
    bind = engine 
)

Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
