from typing import Required
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    """Represents a user in the system."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_user_employee = Column(Boolean, nullable=False, default=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )


class Customer(User):
    """Represents a customer in the system. Extends User"""

    __tablename__ = "customers"

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    email = Column(String, nullable=False, unique=True)
    additional_name = Column(String, nullable=False)
    social_media_page = Column(String, nullable=False)
    is_adult = Column(Boolean)


class Manager(User):
    """Represents a manager in the system. Extends User"""

    __tablename__ = "managers"

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    personal_id = Column(Integer)
    is_senior = Column(Boolean)


class Appointment(Base):
    """Represents an appointment in the system."""

    __tablename__ = "appointments"

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(Integer, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
