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
- **Data Scraping and Collection**: Extract data from web sources and Telegram channels.
- **Data Cleaning and Transformation**: Clean and transform the collected data to ensure consistency and usability.
- **Object Detection using YOLO**: Integrate object detection capabilities to enhance data analysis.
- **Data Warehouse Design and Implementation**: Develop a scalable data warehouse architecture.
- **Data Integration and Enrichment**: Integrate and enrich data for comprehensive analysis and reporting.

## Features

1. **Data Scraping and Collection Pipeline**
   - Collect data from various web sources and Telegram channels.
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
- Docker (optional, for containerized deployment)
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
   - Set up your PostgreSQL database and update the database configuration in `config.py`.

5. **Run ETL/ELT Pipelines**
   ```bash
   python3 run_etl.py
   ```

6. **Run Object Detection**
   ```bash
   python3 run_yolo.py
   ```

## Usage

### Data Scraping
- To start data scraping, run the `scrape_data.py` script.
  ```bash
  python3 scrape_data.py
  ```

### Data Transformation
- To transform the scraped data, run the `transform_data.py` script.
  ```bash
  python3 transform_data.py
  ```

### Object Detection
- To perform object detection using YOLO, run the `run_yolo.py` script.
  ```bash
  python3 run_yolo.py
  ```

### Data Warehouse Operations
- Load and query data within the data warehouse using SQL scripts or a database management tool.

## Contributing

Contributions are welcome! Please create an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
