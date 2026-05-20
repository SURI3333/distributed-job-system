import time

from app.core.celery_app import celery
from app.db.database import SessionLocal
from app.db.models import Job


@celery.task(bind=True, max_retries=3)
def process_job(self, job_id):

    db = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return

        job.status = "Running"
        db.commit()

        print(f"Processing Job {job.id}")

        time.sleep(10)

        job.status = "Completed"
        db.commit()

        print(f"Completed Job {job.id}")

    except Exception as e:

        if job:
            job.status = "Failed"
            db.commit()

        raise self.retry(exc=e, countdown=5)

    finally:
        db.close()