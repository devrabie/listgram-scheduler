# models/ext_tim.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExtTim(Base):
    __tablename__ = 'ext_tim'
    id = Column(Integer, primary_key=True)
    idbot = Column(String)
    updated_at = Column(Integer)
    command = Column(String)
    count =  Column(Integer, default=0)