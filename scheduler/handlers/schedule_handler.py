import time
from datetime import datetime
import pytz
from sqlalchemy.orm import Session
from models.schedule import Schedule
from models.ext_tim import ExtTim
from utils.timezones import CITIES
from utils import telegram_bot  # ستنشئ هذه الوظيفة

def get_current_time(city):
    tz = pytz.timezone(city)
    now = datetime.now(tz)
    return now.strftime('%H:%M')

def process_schedules(db: Session):
    post_summaries = []
    post_logs = []
    insert_entries = []

    for region, cities in CITIES.items():
        for city in cities:
            timezone_name = f"{region}/{city}"
            current_time = get_current_time(timezone_name)

            schedules = db.query(Schedule).filter(
                Schedule.times == current_time,
                Schedule.timezone_set == city,
                getattr(Schedule, datetime.now(pytz.timezone(timezone_name)).strftime('%A')) == '✅'
            ).all()

            for s in schedules:
                clean_cmd = s.command.replace("حزف", "حذف").replace(">", "").replace("<", "")
                # count = get_bot_db_count(s.idbot)  # تفترض أنك كتبت هذه الوظيفة
                count = 0  # استبدل هذا بالقيمة الفعلية
                insert_entries.append(ExtTim(
                    idbot=s.idbot,
                    updated_at=int(time.time()) + 70,
                    command=clean_cmd,
                    count=count
                ))

                if clean_cmd == "نشر":
                    post_logs.append(f"⏰ {s.command} @{s.botusr} ({count})")
                else:
                    post_summaries.append(f"⏰ {s.command} @{s.botusr} ({count})")

    if insert_entries:
        db.bulk_save_objects(insert_entries)
        db.commit()

    # if post_logs:
    #     send_telegram_message(
    #         chat_id="-1001901727110",
    #         text="\n".join(post_logs),
    #         parse_mode="HTML"
    #     )

    return "\n".join(post_summaries)
