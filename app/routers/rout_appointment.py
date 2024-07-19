from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, utils
from app.database import get_db
from ..schemas import AppointmentCreate, AppointmentResponse
from util import logging_setup

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"],  # Adds headers to documentation http://127.0.0.1:8000/redoc
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AppointmentCreate)
def create_appointment(user: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment: models.Appointment = models.Appointment(**user.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    user = get_user(new_appointment.user_id, db).first_name
    logging_setup.log.info(f"User {user} created an appointment")

    return new_appointment


@router.get("/{id}", response_model=AppointmentResponse)
def get_appointment(id: int, db: Session = Depends(get_db)):
    appointment: models.Appointment = db.query(models.Appointment).filter(models.Appointment.id == id).first()

    user = get_user(appointment.user_id, db).first_name
    logging_setup.log.info(f"User {user} requested an appointment")

    return appointment

def get_user(id: int, db: Session = Depends(get_db)):
    user: models.User = db.query(models.User).filter(models.User.id == id).first()
    return user
