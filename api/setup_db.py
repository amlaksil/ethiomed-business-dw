#!/usr/bin/python3
"""
Setup script to create the database tables.
"""
from sqlalchemy import create_engine
from api.models import Base
from api.database import DATABASE_URL


def setup_database():
    """Create database tables based on the defined models."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    setup_database()
