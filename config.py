from pathlib import Path

# Google Cloud configuration
PROJECT_ID = "macro-data-platform1"
BUCKET_NAME = "wb-imf-datalake-1"

# BigQuery datasets
RAW_DATASET = "raw"
STAGING_DATASET = "staging"
ANALYTICS_DATASET = "analytics"

# BigQuery tables
WORLD_BANK_TABLE = f"{PROJECT_ID}.{RAW_DATASET}.world_bank"
IMF_TABLE = f"{PROJECT_ID}.{RAW_DATASET}.imf"

# Local data directory
DATA_DIR = Path("data")

# Local files
WORLD_BANK_FILE = DATA_DIR / "world_bank.parquet"
IMF_FILE = DATA_DIR / "imf.parquet"