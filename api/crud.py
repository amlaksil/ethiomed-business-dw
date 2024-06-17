#!/usr/bin/python3
"""
CRUD (Create, Read, Update, Delete) operations for detection results.
"""
from sqlalchemy.orm import Session
from api import models, schemas


def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    """
    Get detection results from the database with pagination.

    Args:
        db (Session): Database session.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to return.

    Returns:
        List[models.DetectionResult]: List of detection results.
    """
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()


def create_detection_result(
        db: Session, detection_result: schemas.DetectionResultCreate):
    """
    Create a new detection result in the database.

    Args:
        db (Session): Database session.
        detection_result (schemas.DetectionResultCreate): Detection
        result data.

    Returns:
        models.DetectionResult: Created detection result.
    """
    db_detection_result = models.DetectionResult(
        image_path=detection_result.image_path,
        class_id=detection_result.class_id,
        confidence=detection_result.confidence,
        bbox=detection_result.bbox
    )
    db.add(db_detection_result)
    db.commit()
    db.refresh(db_detection_result)
    return db_detection_result
