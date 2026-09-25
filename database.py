# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# DB_USER = "root"
# DB_PASSWORD = "71102" 
# DB_HOST = "127.0.0.1"
# DB_PORT = "3306"
# DB_NAME = "student_db"

# DATABASE_URL = ("mysql+pymysql://root:71102@localhost:3306/student_db")

# engine = create_engine(DATABASE_URL) 

# SessionLocal = sessionmaker (
#     autocommit = False,
#     autoflush = False,
#     bind = engine 
# )

# Base = declarative_base() 

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close() 

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv() 

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL,)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()