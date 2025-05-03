import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# تعريف القاعدة الأساسية للنماذج
Base = declarative_base()

# إعداد بيانات الاتصال بقاعدة البيانات
DB_HOST = '158.220.123.1'
DB_USER = 'Drlistat_bot'
DB_PASSWORD = os.getenv('DB_MakerBots')
DB_NAME = 'MakerBots'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# إنشاء المحرك (Engine)
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    echo=False  # اجعله True إن أردت طباعة استعلامات SQL
)

# إعداد الجلسة
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# دالة للحصول على جلسة قاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
