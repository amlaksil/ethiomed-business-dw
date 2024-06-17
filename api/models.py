#!/usr/bin/python3
"""
SQLAlchemy models for the detection results table.
"""
from sqlalchemy import Column, Integer, String, Float, Text, JSON
from .database import Base


class DetectionResult(Base):
    """
    DetectionResult model to represent detection results in the database.
    """
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    class_id = Column(Float)
    confidence = Column(Float)
    bbox = Column(JSON)
