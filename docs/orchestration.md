# Workflow Orchestration

## Tool

Apache Airflow

---

## DAG Workflow

```text
Extract
   ↓
Transform
   ↓
Load
   ↓
Query
```

---

## Schedule

The workflow executes daily at:

```text
20:00
```

Cron expression:

```text
0 20 * * *
```

---

## Retry Strategy

If a temporary failure occurs:

- Retries: 1
- Retry Delay: 5 Minutes

---

## Logging

The workflow writes processing events to a log file.

Examples:

```text
Extraction Started
Extraction Completed
Transformation Started
Loading Completed
Running Query
Writing Completed
```

The log assists with monitoring and troubleshooting.
