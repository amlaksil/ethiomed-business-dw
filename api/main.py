#!/usr/bin/python3
"""
FastAPI application to manage detection results.
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
from typing import List

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """Ensure the database table is created on startup."""
    models.Base.metadata.create_all(bind=engine)


@app.post("/detection_results/", response_model=schemas.DetectionResult)
def create_detection_result(
        detection_result: schemas.DetectionResultCreate,
        db: Session = Depends(get_db)):
    """
    Create a new detection result.

    Returns:
        schemas.DetectionResult: Created detection result.
    """
    return crud.create_detection_result(
        db=db, detection_result=detection_result)


@app.get("/detection_results/", response_model=List[schemas.DetectionResult])
def read_detection_results(
        skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Read detection results with pagination.

    Args:
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to return.
        db (Session): Database session.

    Returns:
        List[schemas.DetectionResult]: List of detection results.
    """
    results = crud.get_detection_results(db, skip=skip, limit=limit)
    return results
