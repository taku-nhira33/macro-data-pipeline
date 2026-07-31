from world_bank import fetch_world_bank_data
from imf import fetch_imf_data
from storage import upload_to_gcs
from bigquery_loader import load_world_bank_table, load_imf_table


def main():
    print("Starting macroeconomic data pipeline...")

    # Extract
    wb_file = fetch_world_bank_data()
    imf_file = fetch_imf_data()

    # Upload World Bank parquet file
    upload_to_gcs(
        wb_file,
        "data/raw/world_bank/world_bank.parquet"
    )
    
    # Upload IMF parquet file
    upload_to_gcs(
        imf_file,
        "data/raw/imf/imf.parquet"
    )
    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()