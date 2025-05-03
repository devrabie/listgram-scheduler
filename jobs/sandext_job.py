# jobs/sandext_job.py

import datetime
import traceback

from sqlalchemy.orm import Session
from models.ext_tim import ExtTim
from utils.database import get_db as Database
from utils.http_client import post_json
from utils.logger import logger


ADMIN_LOG_CHAT_ID = "-1001901727110"  # يمكن تغييره لاحقاً أو نقله إلى .env


def execute_sandext_job():
    db = Database().get_session()

    try:
        # احصل على المهام المجدولة المناسبة
        tasks = db.query(ExtTim).filter(
            (ExtTim.command.like("%نشر%")) |
            (ExtTim.command == "انشر") |
            (ExtTim.command == "مسح رد")
        ).order_by(ExtTim.Count.asc()).limit(30).all()

        if not tasks:
            logger.info("لا توجد مهام نشر حالياً.")
            return

        report_lines = [
            f"تنفيذ Sandext ({len(tasks)})",
            datetime.datetime.now().strftime("%I:%M %p"),
            ""
        ]

        for idx, task in enumerate(tasks, start=1):
            url = f"https://snd.listgram.org/LestaSrc/dev/{task.idbot}/cron.php?Command={task.command}&update_id={task.id}"
            try:
                response = post_json(url)
                if response.status_code == 200:
                    db.delete(task)
                    db.commit()
                    report_lines.append(f"{idx}. ✅ ID: {task.id}")
                else:
                    db.delete(task)
                    db.commit()
                    report_lines.append(f"{idx}. ⚠️ ({response.status_code}) ID: {task.id}")
            except Exception as e:
                db.delete(task)
                db.commit()
                logger.error(f"خطأ في المهمة ID={task.id}: {e}\n{traceback.format_exc()}")
                report_lines.append(f"{idx}. ❌ ID: {task.id}")

        # طباعة التقرير النهائي
        full_report = "\n".join(report_lines)
        logger.info("تقرير تنفيذ Sandext:\n" + full_report)

    finally:
        db.close()
