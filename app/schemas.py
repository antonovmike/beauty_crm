from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP


class UserBase(BaseModel):
    first_name: str
    second_name: str
    phone: str
    password: str
    is_user_employee: bool


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    created_at: datetime


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
