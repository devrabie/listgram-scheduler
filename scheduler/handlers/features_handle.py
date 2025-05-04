# scheduler/handlers/features_handler.py
import time
import pytz
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.ext_tim import ExtTim

Base = declarative_base()

class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    idbot = Column(String)
    timspy = Column(String)
    timlft = Column(String)
    list = Column(Boolean)
    spy = Column(Boolean)
    lift = Column(Boolean)

def is_spy(db: Session, idbot: str) -> bool:
    """Check if a bot is already marked as 'spy' in ext_tim."""
    return db.query(ExtTim).filter(ExtTim.command == 'spy', ExtTim.idbot == idbot).first() is not None

def is_lift(db: Session, idbot: str) -> bool:
    """Check if a bot is already marked as 'lift' in ext_tim."""
    return db.query(ExtTim).filter(ExtTim.command == 'lift', ExtTim.idbot == idbot).first() is not None

def select_spy(db: Session):
    """Select bots from features table based on timspy, list, and spy flags."""
    current_time = datetime.now(pytz.timezone('UTC')).strftime('%I:%M%p').lower()
    time_plus_90_minutes = datetime.now(pytz.utc).replace(microsecond=0, second=0)
    time_plus_90_minutes = time_plus_90_minutes.astimezone(pytz.timezone('Asia/Baghdad')).strftime('%I:%M%p').lower()
    #time_plus_90_minutes = (datetime.utcnow() + timedelta(minutes=90)).strftime('%I:%M%p').lower()
    #time_plus_90_minutes = time.strftime('%I:%M%p')
    #time_plus_90_minutes = datetime.now().strftime('%I:%M%p').lower()
    print(f"Current time + 90 minutes: {time_plus_90_minutes}")
    text = f"{time_plus_90_minutes} 🗓 : Monitoring  \n==================================\n"
    counter = 1

    features = db.query(Feature).filter(
        Feature.timspy == time_plus_90_minutes,
        Feature.list == True,
        Feature.spy == True
    ).all()

    for feature in features:
        idbot = feature.idbot
        command = 'spy'
        text += f"{counter}-⏰ {idbot} \n"
        counter += 1

        if not is_spy(db, idbot):
            ext_tim_record = ExtTim(idbot=idbot, updated_at=int(time.time()) + 90, command=command)
            db.add(ext_tim_record)
            db.commit()

    return text

def select_lift(db: Session):
    """Select bots from features table based on timlft, list, and lift flags."""
    current_time = datetime.now(pytz.timezone('UTC')).strftime('%I:%M%p').lower()
    time_plus_70_minutes = datetime.now(pytz.utc).replace(microsecond=0, second=0)
    time_plus_70_minutes = time_plus_70_minutes.astimezone(pytz.timezone('Asia/Baghdad')).strftime('%I:%M%p').lower()
    #time_plus_70_minutes = (datetime.utcnow() + timedelta(minutes=70)).strftime('%I:%M%p').lower()
    #time_plus_70_minutes = time.strftime('%I:%M%p')
    #time_plus_70_minutes = datetime.now().strftime('%I:%M%p').lower()
    print(f"Current time + 70 minutes: {time_plus_70_minutes}")
    text = f"{time_plus_70_minutes} 🗓 : Lifted  \n==================================\n"
    counter = 1

    features = db.query(Feature).filter(
        Feature.timlft == time_plus_70_minutes,
        Feature.list == True,
        Feature.lift == True
    ).all()

    for feature in features:
        idbot = feature.idbot
        command = 'lift'
        text += f"{counter}-⏰ {idbot} \n"
        counter += 1

        if not is_lift(db, idbot):
            ext_tim_record = ExtTim(idbot=idbot, updated_at=int(time.time()) + 70, command=command)
            db.add(ext_tim_record)
            db.commit()

    return text

def process_features(db: Session):
    """Main function to process both spy and lift features."""
    spy_text = select_spy(db)
    lift_text = select_lift(db)
    return spy_text + lift_text