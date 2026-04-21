from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = models.User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Usuario creado", "user_id": user.id}