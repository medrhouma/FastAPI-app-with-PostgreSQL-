# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL string for the Postgres database
# In this example, the database name is 'quizApp'
URL_DATABASE = 'postgresql://postgres:hama@localhost:5432/quizApp'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()