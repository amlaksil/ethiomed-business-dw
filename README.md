# Ethiopian Medical Business Data Warehouse

Welcome to the Ethiopian Medical Business Data Warehouse project! This repository contains the code and documentation for building a robust, scalable data warehouse to store, process, and analyze data on Ethiopian medical businesses. The data is sourced from web scraping and Telegram channels, and enhanced with object detection capabilities using YOLO (You Only Look Once).

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves several key components to ensure the data warehouse is effective and efficient:
- **Data Scraping and Collection**: Extract data from Telegram channels.
- **Data Cleaning and Transformation**: Clean and transform the collected data to ensure consistency and usability.
- **Object Detection using YOLO**: Integrate object detection capabilities to enhance data analysis.
- **Data Warehouse Design and Implementation**: Develop a scalable data warehouse architecture.
- **Data Integration and Enrichment**: Integrate and enrich data for comprehensive analysis and reporting.

## Features YOLO model to detect objects in the images

1. **Data Scraping and Collection Pipeline**
   - Collect data from various Telegram channels.
   - Use automated scripts to continuously update the data.

2. **Data Cleaning and Transformation Pipeline**
   - Clean the raw data to remove inconsistencies.
   - Transform the data into a structured format suitable for analysis.

3. **Object Detection using YOLO**
   - Implement YOLO to perform object detection on images.
   - Integrate detected objects into the data warehouse for enhanced analysis.

4. **Data Warehouse Design and Implementation**
   - Design a robust and scalable data warehouse schema.
   - Implement the data warehouse using modern technologies like AWS Redshift, Google BigQuery, or Azure Synapse.

5. **Data Integration and Enrichment**
   - Integrate data from different sources.
   - Enrich the data to add more context and value for analysis.

## Architecture

The high-level architecture of the project includes the following components:

1. **Data Sources**
   - Web scraping scripts and Telegram channel data collectors.

2. **ETL/ELT Pipeline**
   - Extract, Transform, Load (ETL) processes.
   - Extract, Load, Transform (ELT) processes.

3. **Object Detection Module**
   - YOLO-based object detection integration.

4. **Data Warehouse**
   - Centralized storage for all processed data.
   - Schema design and optimization for efficient querying.

## Setup and Installation

### Prerequisites

- Python 3.8+
- PostgreSQL or any preferred database for the data warehouse
- Virtual Environment (venv)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/amlaksil/ethiomed-business-dw
   cd ethiomed-business-dw
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - Set up your PostgreSQL database.

6. **Run Object Detection**
   ```bash
   python3 -m scripts.run_yolo
   ```

## Usage

### Data Scraping
- To start data scraping, run the `telegram_message_scraper.py` script.
  ```bash
  python3 scripts/telegram_message_scraper.py
  ```
- For image scraping, run the `telegram_image_scraper.py`
	```bash
  python3 scripts/telegram_image_scraper.py
	```
### Object Detection
- To perform object detection using YOLO, run the `run_yolo.py` script.
  ```bash
  python3 -m scripts.run_yolo
  ```

### Data Warehouse Operations
- Load and query data within the data warehouse using SQL scripts or a database management tool.

## Contributing

Contributions are welcome! Please create an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
