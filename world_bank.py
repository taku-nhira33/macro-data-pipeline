#Import packages

import pandas as pd
import requests as req
import wbgapi as wb
import pyarrow.parquet as pq
from pathlib import Path

#Set variable names for World Bank Data
GDP = 'NY.GDP.MKTP.CD'
POPL = 'SP.POP.TOTL'
GDP_GROWTH = 'NY.GDP.MKTP.KD.ZG'

#Request World Bank Data and put into dataframe

def fetch_world_bank_data():

    print("Fetching World Bank data...")

    wbtable = wb.data.DataFrame(
        [GDP, POPL, GDP_GROWTH],
        time=range(1960, 2025),
        numericTimeKeys=True,
        labels=True,
        columns='series'
    )

    wbtable = wbtable.rename(columns={
        'NY.GDP.MKTP.CD': 'gdp_current_usd',
        'SP.POP.TOTL': 'population',
        'NY.GDP.MKTP.KD.ZG': 'gdp_growth_pct'
    })

    wbtable = wbtable.reset_index()

    wbtable = wbtable.drop(["Time"], axis=1)

    wbtable = wbtable.rename(columns={
        'Country': 'country_name',
        'economy': 'country_code',
        'time': 'year'
    })

    DATA_DIR = Path("data")
    DATA_DIR.mkdir(exist_ok=True)

    wb_path = DATA_DIR / "world_bank.parquet"

    wbtable.to_parquet(wb_path, index=False)

    print(f"World Bank data saved: {wb_path}")

    return wb_path
