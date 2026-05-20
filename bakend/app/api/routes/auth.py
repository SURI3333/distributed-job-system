from fastapi import APIRouter, HTTPException
from app.db.database import SessionLocal
from app.db.models import User
from app.auth import hash_password, verify_password, create_token

router = APIRouter()


@router.post("/register")
def register(data: dict):

    db = SessionLocal()

    existing = db.query(User).filter(
        User.username == data["username"]
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = User(
        username=data["username"],
        password=hash_password(data["password"])
    )

    db.add(user)
    db.commit()

    db.close()

    return {"message": "Registered successfully"}


@router.post("/login")
def login(data: dict):

    db = SessionLocal()

    user = db.query(User).filter(
        User.username == data["username"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )

    if not verify_password(
        data["password"],
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Wrong password"
        )

    token = create_token({
        "sub": user.username
    })

    db.close()

    return {"token": token}