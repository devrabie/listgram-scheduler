import asyncio
from scheduler.job_manager import start_scheduler

if __name__ == "__main__":
    asyncio.run(start_scheduler())