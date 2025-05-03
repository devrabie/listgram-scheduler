from sqlalchemy import Column, Integer, String
from listgram_scheduler.database import Base

class ExtTim(Base):
    __tablename__ = "ext_tim"

    id = Column(Integer, primary_key=True)
    idbot = Column(String)
    updated_at = Column(Integer)
    command = Column(String)
    count = Column(Integer)
