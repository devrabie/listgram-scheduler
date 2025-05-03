import time
from jobs.sandext_job import execute_sandext_job

def start_scheduler():
    while True:
        try:
            execute_sandext_job()
            print("تم تنفيذ مهمة Sandext بنجاح.")
        except Exception as e:
            print(f"حدث خطأ أثناء تنفيذ مهمة Sandext: {e}")
        time.sleep(60)  # تنفيذ كل دقيقة
