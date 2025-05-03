from utils.database import get_db
from scheduler.handlers.schedule_handler import process_scheduled_posts

def main():
    db = next(get_db())  # استخراج الجلسة
    summary = process_scheduled_posts(db)
    print(summary)

if __name__ == "__main__":
    main()
