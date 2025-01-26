# DeFtunes end to end data pipeline

<a name='1'></a>

## 1 - Introduction

DeFtunes is a new company in the music industry, offering a subscription-based app for streaming songs. Recently, they have expanded their services to include digital song purchases. With this new retail feature, DeFtunes requires a data pipeline to extract purchase data from their new API and operational database, enrich and model this data, and ultimately deliver the comprehensive data model for the Data Analysis team to review and gain insights.

<a name='2'></a>

## 2 - Technical Overview

1. The pipeline follows a **medallion architecture** with a landing, transform and serving zone.
2. The data generated in the pipeline are stored in the company's **data lake** in S3 bucket.
3. The silver layer utilizes **Apache Iceberg** tables, and the gold layer is inside **Redshift**.
4. To ensure the reproducibility of the pipeline, it is implemented with **Terraform**.
5. The data are modeled into a star schema in the serving layer using **dbt**.
6. The pipeline allows the **incremental** ingestion of new data from the data sources.
7. The pipeline is orchestrated with **Apache Airflow**.
8. Data quality checks are implemented to verify the quality of newly ingested and cleansed data.
9. Analytical views should be added on top of the star schema data model.
10. A **Superset** dashboard is added to the architecture, to allow the visualization of the analytical views and insights. <br><br>

![Capstone_Diagram](images/Capstone-diagram.png)

<a name='3'></a>

## 3 - Data Sources

1.  DeFtunes **API** used to gather information on the purchases done by the users of the App and also relevant information about each user.
2.  DeFtunes **Operational RDS** running in RDS with a Postgres engine.

<a name='4'></a>

## 4 - ETL Pipeline with AWS Glue and Terraform

The pipeline contains the following steps:

- An extraction job to get the data from the PostgreSQL Database. This data is stored in the landing zone of the Data Lake.
- An extraction job to get the data from the API endpoints. This data is stored in the landing zone of the Data Lake in JSON format.
- A transformation job that takes the raw data extracted from the PostgreSQL Database, casts some fields to the correct data types, adds some metadata and stores the dataset in Iceberg format.
- A transformation job that takes the JSON data extracted from the API endpoints, normalizes some nested fields, adds metadata and stores the dataset in Iceberg format.
- A job to create schemas in the Data Warehouse hosted in Redshift.

The jobs and the necessary ressources are created using Terraform to guarantee that the infrastructure for each job will be always the same and changes can be tracked easily.

### Serving Zone

In the last layer of the three-tier Data Lake architecture, AWS Redshift is used as a Data Warehouse. The transformations are performed directly inside Redshift. Redshift Spectrum allows to run queries against data stored in S3 without having to load the data into Redshift tables. It requires also using Glue Catalog.

<a name='5'></a>

## 5 - Data Modeling with dbt and Redshift Spectrum

Amazon Redshift connects with Apache Iceberg tables using **Redshift Spectrum**. Redshift Spectrum enables querying files stored in S3 directly from Redshift and allows direct access to Iceberg tables by creating an external schema that references the AWS Glue Data Catalog containing the tables.

dbt connects to Redshift and models the transform layer tables into star schema in the serving layer.

<a name='6'></a>

## 6 - Data Quality with AWS Glue

The data quality checks are performed using **AWS Glue Data Quality**.<br>
The quality checks are defined using **`Data Quality Definition Language (DQDL)`**.

<a name='7'></a>

## 7 - Creating Materialized Views with _dbt_

To address the business questions, we use materialized views. The required data modeling is performed using **dbt** (data build tool).

<a name='8'></a>

## 8 - Orchestration with Apache Airflow

Airflow is used to orchestrate the extraction, transformation, quality checks and modeling the obtained data.

![deftunes_api_dag](./images/deftunes_api_dag.png)

<a name='9'></a>

## 9 - Running the Project

In AWS Console open Cloud9 and create a new environment.
Upload the data and run:

```bash
source ./scripts/setup.sh
```

Deploy the required infrastructure for the three-tier-data lake:

```bash
cd terraform
terraform init
terraform plan
terraform apply -target=module.extract_job
terraform apply -target=module.transform_job
terraform apply -target=module.serving
```

Go to AWS Cloudformation Outputs tab and copy the value of the key `AirflowDNS` and open the link in a browser tab. In the login page, use `airflow` for both, the user and password. In the Airflow UI press the toggle button to unpause the DAG, it should start automatically.

<a name='10'></a>

# 10 - Technologies Used

- **Data Extraction and Transformation**: AWS Glue, Apache Iceberg, Redshift Spectrum, Glue Catalog
- **Data Storage**: S3, Redshift
- **Orchestration**: Apache Airflow
- **Data Modeling**: dbt (Data Build Tool)
- **Visualization**: Apache Superset
- **Infrastructure as Code**: Terraform
  <br><br><br>
  _Project based on the Capstone Project from the specialization ["DeepLearning.AI Data Engineering"](https://www.coursera.org/professional-certificates/data-engineering)_
