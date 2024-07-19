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
    client_id: int
    user_id: int


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
