import time
import pytz
from datetime import datetime
from sqlalchemy.orm import Session
from models.schedule import Schedule
from models.ext_tim import ExtTim
from utils.timezones import CITIES
# from utils.telegram_bot import send_message

def get_current_time_str(timezone_name):
    now = datetime.now(pytz.timezone(timezone_name))
    return now.strftime('%H:%M')

def get_day_column(timezone_name):
    now = datetime.now(pytz.timezone(timezone_name))
    return now.strftime('%A')  # Sunday, Monday...

def get_bot_post_count(bot_id: str) -> int:
    # مثال وهمي - استبدله بكود حقيقي لاحتساب عدد المنشورات في قاعدة بيانات البوت
    return 5

def process_scheduled_posts(db: Session):
    post_logs = []
    summary_logs = []
    insert_records = []

    for region, cities in CITIES.items():
        for city in cities:
            timezone_name = f"{region}/{city}"
            current_time = get_current_time_str(timezone_name)
            day_column = get_day_column(timezone_name)

            filters = {
                Schedule.times: current_time,
                Schedule.timezone_set: city,
                getattr(Schedule, day_column): '✅'
            }

            schedules = db.query(Schedule).filter(*filters).all()

            for sched in schedules:
                clean_cmd = sched.command.replace("حزف", "حذف").replace(">", "").replace("<", "")
                count = get_bot_post_count(sched.idbot)

                insert_records.append(ExtTim(
                    idbot=sched.idbot,
                    updated_at=int(time.time()) + 70,
                    command=clean_cmd,
                    count=count
                ))

                log_line = f"⏰ {sched.command} @{sched.botusr} ({count})"

                if clean_cmd == "نشر":
                    post_logs.append(log_line)
                else:
                    summary_logs.append(log_line)

    if insert_records:
        db.add_all(insert_records)
        db.commit()

    return "\n".join(summary_logs)
