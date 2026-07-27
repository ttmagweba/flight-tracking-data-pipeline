# Flight Tracking Data Pipeline

## Overview
The objective of this project is to automate the collection and processing of flight activity data within a defined geographical area.
 
The pipeline retrieves aircraft information, enriches the dataset with calculated distances from a central location, stores the results in a normalized database structure, and generates daily reports on selected commercial aircraft operating near the configured location.

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

## Work Flow

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
