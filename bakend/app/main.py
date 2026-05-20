from fastapi import FastAPI
from app.api.routes.jobs import router as jobs_router
from app.api.routes.auth import router as auth_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Distributed Job Queue System"
)

app.include_router(auth_router)
app.include_router(jobs_router)