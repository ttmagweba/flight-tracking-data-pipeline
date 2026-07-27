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

## Project Architecture

See:

```text
docs/architecture.md
```

---

## Data Flow

See:

```text
docs/data_flow.md
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

## Key Data Engineering Concepts Demonstrated

- REST API Integration
- Batch ETL Processing
- Data Cleaning
- Data Transformation
- Geospatial Data Processing
- Relational Database Design
- Database Normalization
- Data Modeling
- Apache Airflow Orchestration
- Logging and Monitoring
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
├── docs/
│   ├── architecture.md
│   ├── database_design.md
│   ├── orchestration.md
│   ├── data_flow.md
│   └── screenshots/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

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
