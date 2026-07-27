# Flight Tracking Data Pipeline

## Overview
Built an end-to-end batch ETL pipeline that ingests live aircraft tracking data from a REST API, enriches records using geospatial calculations, stores data in a normalized relational database, and automatically generates daily analytical CSV reports through Apache Airflow orchestration.

The pipeline retrieves live aircraft data around Johannesburg, enriches each record by calculating its distance from a predefined location using the Haversine formula, and stores the data in a normalized SQLite database for SQL-based analysis.

## Project Objective

The goal of this project was to design an end-to-end ETL pipeline that demonstrates industry-standard data engineering practices including automated workflow orchestration, relational data modeling, error handling, and analytical reporting using live aircraft data.

---

## Technology Stack

- Python
- Pandas
- NumPy
- Requests
- SQLite
- Apache Airflow

---

## Project Architecture
![](docs/screenshots/architecture.png)

See:

```text
docs/architecture.md
```

---

## Workflow

See:

```text
docs/work_flow.md
```

---

## Database Design

See:

```text
docs/database_design.md
```

---

## Workflow Orchestration

See:

```text
docs/orchestration.md
```
---

## Screenshots

### Airflow DAG
![](docs/screenshots/dag_graph.png)

### Successful DAG Run

![](docs/screenshots/successful_run.png)

### Database Tables

![](docs/screenshots/database_normalized_flights.png)

For Other Tables See:

```text
docs/screenshots/database_tables.png
docs/screenshots/database_aicraft.png
docs/screenshots/database_model.png
```

### Query Results

![](docs/screenshots/query_results.png)
See:

### Log file

![](docs/screenshots/log_output.png)

---

## Features

- ETL Pipeline
- Apache Airflow
- REST API Integration
- Data Cleaning
- Feature Engineering
- Geospatial Processing
- Relational Database Design
- Database Normalization
- SQL Analytics
- Logging
- Error Handling
- Automated Reporting

---

## Repository Structure

```text
flight-tracking-data-pipeline/
│
├── dags/
│   └── flights_tracking.py
│
├── database/
│   └── flights_tracking.db
│
├── docs/
│   ├── architecture.md
│   ├── database_design.md
│   ├── orchestration.md
│   ├── work_flow.md
│   └── screenshots/
│
├── logs/
│   └── log_file.txt
│
├── queryoutput/
│   └── results.csv
│
├── .gitignore
├── README.md
└── requirements.txt
```

---
## Getting Started

### Clone the repository

```bash
git clone https://github.com/<username>/flight-tracking-data-pipeline.git
cd flight-tracking-data-pipeline
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start Apache Airflow

```bash
airflow standalone
```

### Trigger the DAG

From the Airflow UI, trigger the `Flights_Tracking` DAG.

---

## Future Enhancements

- PostgreSQL Migration
- Docker Containerization
- Cloud Deployment
- Data Quality Validation
- Dashboard Visualizations
- CI/CD Implementation
- Data Warehouse Integration

---

## Author

Thabani Magweba
