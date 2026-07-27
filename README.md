# Flight Tracking Data Pipeline

## Overview

This project automates the collection and processing of live aircraft tracking data.

The pipeline extracts flight information from the Airplanes Live API, performs data cleaning and enrichment, loads the results into a normalized database, and generates a daily analytical report.

The workflow is orchestrated using Apache Airflow and runs automatically every day at 20:00.

---

## Technology Stack

- Python
- Pandas
- NumPy
- Requests
- SQLite
- Apache Airflow

---

## Pipeline Architecture

Extract → Transform → Load → Query

---

## Features

- REST API data extraction
- Data quality handling
- Geospatial distance calculations
- Database normalization
- Scheduled batch processing
- Logging and monitoring
- Automated reporting

---

## Project Workflow

1. Extract flight data from API.
2. Save raw source data.
3. Select required attributes.
4. Remove records with missing data.
5. Calculate distance from centre point.
6. Load data into database.
7. Normalize database tables.
8. Execute analytical query.
9. Append results to output file.
10. Log all processing events.

---

## Schedule

The Airflow DAG executes daily at 20:00.

```text
0 20 * * *
