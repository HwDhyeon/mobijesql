from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mobijesql.env import mysql

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{mysql.user}:{mysql.password}@{mysql.host}:{mysql.port}/{mysql.db}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
