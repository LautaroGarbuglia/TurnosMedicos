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

@router.post("/appointments")
def create_appointment(user_id: int, doctor_id: int, date: str, db: Session = Depends(get_db)):
    appointment = models.Appointment(
        user_id=user_id,
        doctor_id=doctor_id,
        date=date
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return {"message": "Turno creado", "id": appointment.id}

@router.delete("/appointments/{id}")
def delete_appointment(id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).get(id)
    
    if not appointment:
        return {"error": "Turno no encontrado"}
    
    db.delete(appointment)
    db.commit()
    return {"message": "Turno cancelado"}