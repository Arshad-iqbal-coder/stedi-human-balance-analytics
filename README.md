# STEDI Human Balance Analytics

## Project Overview

This project implements a data lakehouse solution for STEDI Step Trainer sensor data using AWS Glue, Athena, and Amazon S3. The pipeline processes raw customer, accelerometer, and step trainer data through Landing, Trusted, and Curated zones to create machine learning-ready datasets.

---

## Architecture

![Architecture Diagram](screenshots/architecture_diagram.png)

## AWS Services Used

* Amazon S3
* AWS Glue Studio
* AWS Glue Data Catalog
* Amazon Athena
* PySpark
* SQL

---

## Architecture

### Landing Zone

Raw JSON data stored in Amazon S3:

* customer_landing
* accelerometer_landing
* step_trainer_landing

### Trusted Zone

Filtered datasets containing only research-consented users:

* customer_trusted
* accelerometer_trusted
* step_trainer_trusted

### Curated Zone

Machine learning-ready datasets:

* customer_curated
* machine_learning_curated

---

## Glue ETL Jobs

1. customer_landing_to_trusted.py
2. accelerometer_landing_to_trusted.py
3. customer_trusted_to_curated.py
4. step_trainer_trusted.py
5. machine_learning_curated.py

---

## How to Run

1. Upload the source JSON files to the corresponding S3 landing folders.
2. Create Athena external tables using:

   * customer_landing.sql
   * accelerometer_landing.sql
   * step_trainer_landing.sql
3. Run the Glue jobs in the following order:

   * customer_landing_to_trusted
   * accelerometer_landing_to_trusted
   * customer_trusted_to_curated
   * step_trainer_trusted
   * machine_learning_curated
4. Validate outputs using Athena queries.

---

## Final Row Counts

| Table                    | Row Count |
| ------------------------ | --------: |
| customer_landing         |       956 |
| accelerometer_landing    |     81273 |
| step_trainer_landing     |     28680 |
| customer_trusted         |       482 |
| accelerometer_trusted    |     40981 |
| customer_curated         |       482 |
| step_trainer_trusted     |     14460 |
| machine_learning_curated |     43681 |

---

## Validation Screenshots

The repository contains Athena query screenshots for:

### Landing Zone

* customer_landing_count.png
* customer_landing_blank_research_date.png
* accelerometer_landing_count.png
* step_trainer_landing_count.png

### Trusted Zone

* customer_trusted_count.png
* accelerometer_trusted_count.png

### Curated Zone

* customer_curated_count.png
* step_trainer_trusted_count.png
* machine_learning_curated_count.png

Additional screenshots showing sample records from each table are also included.

---

## Skills Demonstrated

- AWS Glue
- Amazon S3
- Amazon Athena
- ETL Development
- Data Engineering
- Data Lakehouse Architecture
- PySpark
- SQL
- Cloud Computing
- Data Governance

---
## Project Outcomes

- Built an end-to-end AWS Data Lakehouse pipeline.
- Processed 80,000+ sensor records.
- Implemented privacy-aware filtering using research consent data.
- Created machine-learning-ready curated datasets.
- Validated transformations using Amazon Athena.

## Repository Structure

```text
.
├── README.md

├── sql/
│   ├── customer_landing.sql
│   ├── accelerometer_landing.sql
│   └── step_trainer_landing.sql

├── glue_jobs/
│   ├── customer_landing_to_trusted.py
│   ├── accelerometer_landing_to_trusted.py
│   ├── customer_trusted_to_curated.py
│   ├── step_trainer_trusted.py
│   └── machine_learning_curated.py

└── screenshots/
    ├── customer_landing_count.png
    ├── customer_landing_blank_research_date.png
    ├── accelerometer_landing_count.png
    ├── step_trainer_landing_count.png
    ├── customer_trusted_count.png
    ├── accelerometer_trusted_count.png
    ├── customer_curated_count.png
    ├── step_trainer_trusted_count.png
    ├── machine_learning_curated_count.png
    └── additional table preview screenshots
```
