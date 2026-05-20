from app.db.database import SessionLocal
from app.db.models import Job
from app.workers.tasks import process_job


def create_job(job_type, payload, priority):
    db = SessionLocal()

    job = Job(
        job_type=job_type,
        payload=payload,
        priority=priority
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    process_job.delay(job.id)

    db.close()

    return job