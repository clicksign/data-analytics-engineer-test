#%%
""" Extracts data from CSV files and loads it into a SQLite database."""

import os
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("../case_database.sqlite")

# Create a schema named 'raw'
conn.execute("ATTACH DATABASE 'raw.sqlite' AS raw")

# Get a list of CSV files in the current Data folder
csv_files = [file for file in os.listdir("Data/") if file.endswith(".csv")]

# For each CSV file
for csv_file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f"Data/{csv_file}")

    # Get the table name from the CSV file name
    table_name = os.path.splitext(csv_file)[0] + "_raw"

    # Insert the data into the database
    df.to_sql(f"raw.{table_name}", conn, if_exists="replace", index=False)

# Close the connection
conn.close()
# %%
