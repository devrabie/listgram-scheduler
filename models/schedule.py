from sqlalchemy import Column, Integer, String, Time, Boolean
from utils.database import Base

class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    idbot = Column(String)
    botusr = Column(String)
    command = Column(String)
    times = Column(String)
    timezone_set = Column(String)
    Sunday = Column(String)
    Monday = Column(String)
    Tuesday = Column(String)
    Wednesday = Column(String)
    Thursday = Column(String)
    Friday = Column(String)
    Saturday = Column(String)
