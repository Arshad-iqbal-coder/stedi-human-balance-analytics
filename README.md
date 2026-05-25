# STEDI Human Balance Analytics

## Project Overview
This project builds a data lakehouse solution for STEDI Step Trainer sensor data using AWS services. The goal is to process raw IoT and mobile sensor data into curated datasets that can be used for machine learning model training.

---

# AWS Services Used
- AWS S3
- AWS Glue
- AWS Athena
- PySpark
- SQL

---

# Architecture

## Landing Zone
Raw JSON data stored in S3:
- customer_landing
- accelerometer_landing
- step_trainer_landing

## Trusted Zone
Filtered data containing only research-consented users:
- customer_trusted
- accelerometer_trusted
- step_trainer_trusted

## Curated Zone
Machine learning ready datasets:
- customer_curated
- machine_learning_curated

---

# Glue ETL Jobs
1. customer_landing_to_trusted  
2. accelerometer_landing_to_trusted  
3. customer_curated_job  
4. step_trainer_trusted_job  
5. machine_learning_curated_job  

---

# Final Row Counts

| Table | Row Count |
|---|---|
| customer_landing | 956 |
| accelerometer_landing | 81273 |
| step_trainer_landing | 28680 |
| customer_trusted | 482 |
| accelerometer_trusted | 40981 |
| customer_curated | 482 |
| step_trainer_trusted | 14460 |
| machine_learning_curated | 40981 |

---

# Project Workflow
1. Raw JSON data uploaded to Amazon S3.
2. External tables created in Athena.
3. AWS Glue ETL jobs used to create trusted datasets.
4. Curated datasets generated for machine learning.
5. Athena used for validation and querying.

---

# Key Concepts Learned
- Data Lakehouse Architecture
- ETL Pipelines using AWS Glue
- Spark SQL Transformations
- Data Governance and Privacy Filtering
- Distributed Joins and Event Processing
- Athena Query Validation

---

# Repository Structure

```text
.
├── landing_tables/
├── glue_jobs/
├── screenshots/
└── README.md
