# 🎧 Spotify ETL System

A fully automated, serverless ETL pipeline built using **Python**, **AWS Lambda**, **Snowflake**, and the **Spotify API** to ingest, transform, and store Spotify playlist data for real-time analytics and reporting.

## 🚀 Overview

This project extracts song, artist, and album metadata from a Spotify playlist and automates the ingestion and transformation process using scalable, cloud-native services. The system significantly reduces manual data handling by 90% and enables real-time analytics through optimized Snowflake queries and automated data quality checks.

## 🔧 Tech Stack

- **Languages & Libraries**: Python, Pandas, Spotipy
- **Cloud**: AWS Lambda, S3, CloudWatch
- **Data Warehouse**: Snowflake, Snowpipe
- **Orchestration & Monitoring**: AWS CloudWatch
- **ETL Workflow**: Custom ETL scripts with validation, transformation, and schema enforcement

## 🧩 Pipeline Components

### 1. Data Extraction
- Uses Spotify API via Spotipy to extract:
  - Song metadata
  - Album info
  - Artist profiles
- **Script**: `spotify_data_extraction.py`
- **Output**: Raw data CSVs (`songs`, `albums`, `artists`)

### 2. Data Transformation
- Cleans and enriches data by:
  - Handling duplicates
  - Extracting date/time features
  - Detecting outliers and categorizing song duration
  - Calculating age of each song
- **Script**: `spotify_data_transformation.py`, `utils.py`

### 3. Data Loading
- Data is loaded to **AWS S3**, from where **Snowpipe** auto-ingests into Snowflake staging tables
- Schema validation and query optimization improve performance and integrity
- Monitoring via **CloudWatch**

## ✅ Key Features

- 🔁 **Automated ETL**: Serverless ingestion using Lambda and Snowpipe
- 📊 **Real-Time Analytics**: Data is transformed and ready for dashboarding in near real-time
- 🔍 **Data Integrity**: Includes schema enforcement, anomaly detection, and validation layers


## 📈 Sample Use Cases

- Understanding playlist trends over time
- Identifying outlier tracks based on duration or popularity
- Real-time reporting on new song additions
- Enabling downstream ML models on music metadata
