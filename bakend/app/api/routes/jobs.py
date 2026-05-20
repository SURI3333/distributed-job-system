from fastapi import APIRouter
from app.services.job_service import create_job
from app.db.database import SessionLocal
from app.db.models import Job

router = APIRouter()


@router.post("/jobs")
def submit_job(data: dict):
    return create_job(
        data["job_type"],
        data["payload"],
        data["priority"]
    )


@router.get("/jobs")
def get_jobs():
    db = SessionLocal()
    jobs = db.query(Job).all()
    db.close()
    return jobs