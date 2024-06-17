#!/usr/bin/python3
"""
Pydantic schemas for detection results.
"""
from pydantic import BaseModel
from typing import List, Union


class DetectionResultBase(BaseModel):
    """
    Base schema for detection results.
    """
    image_path: str
    class_id: float
    confidence: float
    bbox: List[Union[int, float]]  # bbox is a list of numbers


class DetectionResultCreate(DetectionResultBase):
    """
    Schema for creating a detection result.
    """
    pass


class DetectionResult(DetectionResultBase):
    """
    Schema for returning a detection result.
    """
    id: int

    class Config:
        orm_mode = True
