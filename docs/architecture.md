# Architecture

## High-Level Architecture

```text
                +------------------+
                | Airplanes.live   |
                | REST API         |
                +--------+---------+
                         |
                         v
                     Extract
                         |
                         v
                 Source Data CSV
                         |
                         v
                    Transform
                         |
                         v
               Transformed Data CSV
                         |
                         v
                       Load
                         |
                         v
              Normalized SQLite DB
                         |
                         v
                 Analytical Query
                         |
                         v
                  Results Output
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
