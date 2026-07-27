# Database Design

## Overview

The database uses a normalized structure to reduce data duplication and improve maintainability.

---

## Entity Relationship Diagram

```text
+-------------+
|   Model     |
+-------------+
| model_id PK |
| type        |
| description |
+------+------+
       |
       |
       |
+------v------+
|  Aircraft   |
+-------------+
| aircraft_id |
| icao_id     |
| registration|
| model_id FK |
+------+------+
       |
       |
       |
+------v---------------+
| Normalized_Flights   |
+----------------------+
| flight_id PK         |
| date                 |
| alt_baro             |
| gs                   |
| ias                  |
| tas                  |
| mach                 |
| true_heading         |
| baro_rate            |
| lat                  |
| lon                  |
| seen                 |
| distance_frm_centre  |
| aircraft_id FK       |
| model_id FK          |
+----------------------+
```

---

## Model Table

Stores aircraft model information.

### Columns

- model_id (Primary Key)
- type
- description

---

## Aircraft Table

Stores unique aircraft information.

### Columns

- aircraft_id (Primary Key)
- icao_id
- registration
- model_id (Foreign Key)

---

## Normalized Flights Table

Stores individual flight observations.

### Columns

- flight_id (Primary Key)
- date
- alt_baro
- gs
- ias
- tas
- mach
- true_heading
- baro_rate
- lat
- lon
- seen
- distance_frm_centre
- aircraft_id (Foreign Key)
- model_id (Foreign Key)

---
