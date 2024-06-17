#!/usr/bin/python3
"""
Script to load detection results data from a CSV file into the database.
"""
from os import getenv
import json
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from .database import Base, SessionLocal
from .models import DetectionResult


def load_data(csv_path):
    """
    Load detection results from a CSV file into the database.

    Args:
        csv_path (str): Path to the CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Rename the columns to match the database schema
    df.rename(columns={'class': 'class_id'}, inplace=True)

    # Create a database session
    db = SessionLocal()

    try:
        for _, row in df.iterrows():
            # Parse bbox from string to list
            bbox_list = json.loads(row['bbox'])

            # Create a DetectionResult object
            detection_result = DetectionResult(
                image_path=row['image_path'],
                class_id=row['class_id'],
                confidence=row['confidence'],
                bbox=bbox_list
            )
            # Add to the session
            db.add(detection_result)

        # Commit the session to write the data to the database
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    # Path to your CSV file
    csv_path = getenv("RESULT_FILE_PATH", "data/detection_results.csv")
    load_data(csv_path)
