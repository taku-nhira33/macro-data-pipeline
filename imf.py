#Import packages

import pandas as pd
import requests as req
import imfp
import pyarrow.parquet as pq
from pathlib import Path

# Requesting IMF CPI data
def fetch_imf_data():

    print("Fetching IMF data...")

    imf_data = imfp.imf_dataset(
        database_id="CPI",
        frequency=["A"],  # Annual frequency
        index_type=["CPI"],  # Consumer Price Index
        type_of_transformation=["IX"],
        start_year=2002,
        end_year=2024
    )

    # Rename columns for consistency
    imf_data = imf_data.rename(columns={
        'country': 'country_code',
        'time_period': 'year'
    })


    # Save data locally as parquet

    DATA_DIR = Path("data")
    DATA_DIR.mkdir(exist_ok=True)

    imf_path = DATA_DIR / "imf.parquet"

    imf_data.to_parquet(imf_path, index=False)

    print(f"IMF data saved: {imf_path}")

    return imf_path



