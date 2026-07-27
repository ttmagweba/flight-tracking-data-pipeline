# Flight Tracking Data Pipeline

## Overview
Built an end-to-end batch ETL pipeline that ingests live aircraft tracking data from a REST API, enriches records using geospatial calculations, stores data in a normalized relational database, and automatically generates daily analytical reports through Apache Airflow orchestration.

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

## Screenshots

### Airflow DAG

See:

```text
docs/screenshots/dag_graph.png
```

### Successful DAG Run

See:

```text
docs/screenshots/successful_run.png
```


### Database Tables

See:

```text
docs/screenshots/database_tables.png
docs/screenshots/database_aicraft.png
docs/screenshots/database_model.png
docs/screenshots/database_normalized_flights.png
```

### Query Results

See:

```text
docs/screenshots/query_results.png
```

### Log file

See:

```text
docs/screenshots/log_output.png
```

---

## Features

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
