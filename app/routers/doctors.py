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

@router.get("/doctors")
def get_doctors(db: Session = Depends(get_db)):
    doctors = db.query(models.Doctor).all()
    return doctors