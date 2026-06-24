"""
Declarative base for all SQLAlchemy models.
Import this base in every model module.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
