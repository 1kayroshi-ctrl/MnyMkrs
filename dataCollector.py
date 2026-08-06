
""" 
stock market data collector module
Connect to postgres database and collect stock market data
Then modify and store the data in the database
"""


# Setup client for Finnhub API (not in use currently)
# # plug = finnhub.Client(api_key=key)
# import finnhub
# key = "INSERT_YOUR_KEY_HERE"

import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
from sqlalchemy import create_engine  # used to write to the database on postgresSQL


# connect to the database raw-stock-data on postgresSQL
engine = create_engine(
    "postgresql://postgres:password@localhost:5432/databsename_here"
)
with engine.connect() as conn:
    print("Connected successfully!")

#list of tickers to download (companies in the S&P 500 Materials secotr)
mat_tkrs = [ 
    "LIN", "NEM", "FCX", "SHW", "CRH", "ECL", "APD", "CTVA","NUE","VMC","MLM","STLD","PPG",
    "SW","DOW","AMCR", "PKG",  "IP","IFF", "DD", "CF", "BALL",  "LYB",  "ALB", "AVY", "MOS"
]
"""
pram: ticker: str
This function downloads stock data for a given ticker from Yahoo Finance, processes it, and stores it in a determinded PostgreSQL database.
Data is of yr:2016 to 2023 and the relevant columns are selected and renamed to match the SQL table structure. 
The processed data is then appended to the "stock_prices" table in the "raw-stock-data" database.

Same code was reused to download data for test data (2023-2024)

"""
def download_to_db(ticker): 

    # Download ticker
    df = yf.download(
        ticker,
        start="2016-01-01",
        end="2023-01-01",
        auto_adjust=False
    )
    print("downloaded data for ticker: ", ticker)

    # remove redundant ticker Row
    df.columns = df.columns.get_level_values(0)

    # move tiker symbol into a normalized column format
    df = df.reset_index()
    df["ticker"] = ticker

    # selected columns in the order for SQL table
    df = df[
        [
            "ticker",
            "Date",
            "Open",
            "Close",
            "High",
            "Low",
            "Volume"
        ]
    ]
    
    # match the column names to the SQL table
    df.columns = [
        "ticker",
        "date",
        "open",
        "close",
        "high",
        "low",
        "volume"
    ]
   
    # Add the data to SQL table stock_prices in the database raw-stock-data 
    df.to_sql(
        name="stock_prices_data", #replace with your table name
        con=engine,
        if_exists="append",
        index=False
    )
    print("data for ticker: ", ticker, " added ")


# Loop through the list of tickers and download data for each ticker, then store it in the database
for ticker in mat_tkrs:
    download_to_db(ticker)
