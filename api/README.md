# API Documentation

This section provides detailed documentation for the API endpoints available in the Ethiomed Business Data Warehouse application. The application is built using FastAPI and provides RESTful endpoints for managing detection results.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Endpoints](#endpoints)
- [Create Detection Result](#create-detection-result)
- [Read Detection Results](#read-detection-results)
- [Data Models](#data-models)
- [Error Handling](#error-handling)

## Overview

The Ethiomed Business Data Warehouse API allows you to create and read detection results stored in a PostgreSQL database. Detection results include information such as the image path, class ID, confidence score, and bounding box coordinates.

## Setup

To set up and run the API, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create a Python virtual environment and activate it:
    ```sh
    python3 -m venv dw-env
    source dw-env/bin/activate
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database by providing the following environment variables:
    ```sh
    export PG_USER=<your_postgres_username>
    export PG_PASSWORD=<your_postgres_password>
    export PG_HOST=<your_postgres_host>
    export PG_DB=<your_postgres_db_name>
    ```
5. Create the database tables:
    ```sh
    python3 setup_db.py
    ```
6. Run the FastAPI application:
    ```sh
    uvicorn api.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Create Detection Result

- **Endpoint:** `/detection_results/`
- **Method:** `POST`
- **Description:** Create a new detection result.

**Request Body:**
```json
{
    "image_path": "path/to/image.jpg",
    "class_id": 1.0,
    "confidence": 0.85,
    "bbox": [100, 200, 300, 400]
}
```

**Response:**
```json
{
    "id": 1,
    "image_path": "path/to/image.jpg",
    "class_id": 1.0,
    "confidence": 0.85,
    "bbox": [100, 200, 300, 400]
}
```

### Read Detection Results

- **Endpoint:** `/detection_results/`
- **Method:** `GET`
- **Description:** Retrieve a list of detection results with pagination.

**Query Parameters:**
- `skip` (int, optional): Number of records to skip. Default is 0.
- `limit` (int, optional): Maximum number of records to return. Default is 10.

**Response:**
```json
[
    {
        "id": 1,
        "image_path": "path/to/image.jpg",
        "class_id": 1.0,
        "confidence": 0.85,
        "bbox": [100, 200, 300, 400]
    },
    ...
]
```

## Data Models

### DetectionResultBase

- `image_path` (str): Path to the image file.
- `class_id` (float): ID of the detected class.
- `confidence` (float): Confidence score of the detection.
- `bbox` (List[Union[int, float]]): Bounding box coordinates as a list of numbers.

### DetectionResultCreate

Inherits from `DetectionResultBase`.

### DetectionResult

Inherits from `DetectionResultBase` and adds:
- `id` (int): Unique identifier for the detection result.

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request. Some common status codes include:

- `200 OK`: The request was successful.
- `201 Created`: The resource was successfully created.
- `400 Bad Request`: The request was invalid or cannot be served.
- `404 Not Found`: The requested resource could not be found.
- `500 Internal Server Error`: An error occurred on the server.

In case of an error, the API will return a JSON response with an `error` key containing a message describing the error.

**Example Error Response:**
```json
{
    "detail": "Record not found"
}
```
