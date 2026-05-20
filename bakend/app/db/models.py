from sqlalchemy import Column, Integer, String, JSON
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_type = Column(String)
    payload = Column(JSON)
    priority = Column(String)
    status = Column(String, default="Pending")
    retries = Column(Integer, default=0)