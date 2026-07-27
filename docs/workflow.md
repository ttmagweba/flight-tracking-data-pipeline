# Workflow

## Extract

The extraction process performs the following steps:

1. Send a request to the Airplanes Live API.
2. Validate the response.
3. Convert JSON data to a Pandas DataFrame.
4. Save raw data to a CSV file.

### Error Handling

The extraction phase handles:

- HTTP Errors
- Timeout Errors
- Connection Errors
- Empty API Responses

---

## Transform

The transformation phase performs:

### Column Selection

Retains only required fields from the source dataset.

### Data Cleaning

Records containing null values are removed.

### Column Standardization

The source column:

```text
desc
```

is renamed to:

```text
description
```

### Data Enrichment

Aircraft distance from the configured centre point is calculated using latitude and longitude coordinates.

Additional field created:

```text
distance_frm_centre
```

### Audit Tracking

A processing date is added to every record.

---

## Load

The transformed data is loaded into a staging table before being normalized into relational tables.

---

## Query

Following the load process, an analytical query is executed and the results are appended to a historical output file.
