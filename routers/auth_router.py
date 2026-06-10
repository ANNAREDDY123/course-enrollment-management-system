from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.models import User
from schemas.schemas import UserRegister, UserLogin
from auth.auth_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserRegister,
             db: Session = Depends(get_db)):

    existing = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Username already exists"
        )

    db_user = User(
        username=user.username,
        password=user.password,
        role=user.role
    )

    db.add(db_user)
    db.commit()

    return {"message": "User registered"}


@router.post("/login")
def login(user: UserLogin,
          db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            401,
            "Invalid username"
        )

    if db_user.password != user.password:
        raise HTTPException(
            401,
            "Invalid password"
        )

    token = create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
