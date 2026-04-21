from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, auth, doctors, appointments

Base.metadata.create_all(bind=engine)
from app.database import SessionLocal
from app import models

db = SessionLocal()

# Solo carga médicos si no hay ninguno
if db.query(models.Doctor).count() == 0:
    db.add_all([
        models.Doctor(name="Dr. Pérez", specialty="Clínico"),
        models.Doctor(name="Dra. Gómez", specialty="Pediatra"),
        models.Doctor(name="Dr. López", specialty="Cardiólogo")
    ])
    db.commit()

db.close()

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
