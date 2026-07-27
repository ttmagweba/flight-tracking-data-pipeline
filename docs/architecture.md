# Architecture

## High-Level Architecture

```text

             Airplanes Live API
                     │
                     ▼
             Extract Raw Data
                     │
                     ▼
            Source CSV File
                     │
                     ▼
          Data Cleaning & Validation
                     │
                     ▼
      Distance Calculation (Haversine)
                     │
                     ▼
         Transformed CSV Dataset
                     │
                     ▼
          Load into SQLite Database
                     │
                     ▼
      Normalize into Relational Tables
                     │
                     ▼
             SQL Analytical Query
                     │
                     ▼
           Results Exported to CSV
```

## Components

### Data Source

The Airplanes Live API provides aircraft tracking information within a defined radius of a geographic location.

### ETL Pipeline

The ETL process extracts, transforms, enriches, and loads aircraft tracking data into a relational database.

### Database

SQLite is used to store normalized aircraft and flight data.

### Orchestration

Apache Airflow schedules and manages workflow execution.

### Reporting

A SQL query produces a daily report which is appended to an output file.
