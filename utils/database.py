# app/core/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

class Database:
    def __init__(self):
        self.host = '158.220.123.1'
        self.username = 'Drlistat_bot'
        self.password = os.getenv('DB_MakerBots')
        self.database = 'MakerBots'
        self.engine = None
        self.SessionLocal = None

        self.init_engine()

    def init_engine(self):
        DATABASE_URL = f"mysql+mysqlconnector://{self.username}:{self.password}@{self.host}/{self.database}"

        self.engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=10) # تعيين حجم التجمع والتدفق الزائد
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        if not self.SessionLocal:
            self.init_engine()
        return self.SessionLocal()

    def close_session(self, session):
        session.close()

def get_db():
    db_instance = Database()
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db_instance.close_session(db)
