#!/usr/bin/python3
"""
Database configuration and session management.
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Fetching database credentials from environment variables
username = getenv('PG_USER')
password = getenv('PG_PASSWORD')
host = getenv('PG_HOST')
dbname = getenv('PG_DB')

# Database URL
DATABASE_URL = f"postgresql://{username}:{password}@{host}/{dbname}"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal factory for creating new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the declarative models
Base = declarative_base()


def get_db():
    """Yield a database session and close it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
