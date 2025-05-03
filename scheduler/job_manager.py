from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from jobs.example_job import run_example_job
import asyncio

async def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(run_example_job, CronTrigger(minute="*"))  # كل دقيقة
    scheduler.start()
    print("Scheduler started. Running...")

    try:
        await asyncio.Event().wait()  # Keeps the event loop running
    except (KeyboardInterrupt, SystemExit):
        pass

