from datetime import datetime
from pydantic import BaseModel


class AppointmentBase(BaseModel):
    title: str  # Client's name
    author: str  # Person who made an Appointment
    was_held: bool
    date_and_time: datetime


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
