# Import packages

from google.cloud import bigquery


# Google Cloud configuration

PROJECT_ID = "macro-data-platform1"


# Authenticate BigQuery

client = bigquery.Client(project=PROJECT_ID)


# Configure the load job

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    autodetect=True,
)


# Create load function

def load_to_bigquery(table_id, uri):

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config
    )

    load_job.result()

    print(f"Data loaded into {table_id}.")


# Load World Bank data

def load_world_bank_table():

    load_to_bigquery(
        "macro-data-platform1.raw.world_bank",
        "gs://wb-imf-datalake-1/data/raw/world_bank/world_bank.parquet",
    )


# Load IMF data

def load_imf_table():

    load_to_bigquery(
        "macro-data-platform1.raw.imf",
        "gs://wb-imf-datalake-1/data/raw/imf/imf.parquet",
    )