#%%
""" Extracts data from CSV files and loads it into a SQLite database."""

import os
import sqlite3
import json
import re
import pandas as pd


def generic_read_csv(filepath):
    """
    Reads a CSV file into a Pandas DataFrame and normalizes JSON data if necessary."""
    # Read the CSV file
    _df = pd.read_csv(filepath)

    # Drop column Unnamed: 0 if exists
    if "Unnamed: 0" in _df.columns:
        _df = _df.drop("Unnamed: 0", axis=1)

    # Iterate over the columns in the DataFrame
    for col in _df.columns:
        # Check if the column contains JSON data
        is_json = bool(re.match(r"^\s*\{.*\}\s*$", str(_df[col].iloc[0])))

        # Normalize the JSON data if necessary
        if is_json:
            normalized_df = pd.json_normalize(_df[col].apply(json.loads))
            _df = pd.concat([_df, normalized_df], axis=1)
            _df = _df.drop(col, axis=1)
    return _df


# Connect to the SQLite database
conn = sqlite3.connect("../case_database.sqlite")

# Create a schema named 'raw'
conn.execute("ATTACH DATABASE 'raw.sqlite' AS raw")

# Get a list of CSV files in the current Data folder
csv_files = [file for file in os.listdir("Data/") if file.endswith(".csv")]

# For each CSV file
for csv_file in csv_files:
    # Read the CSV file into a DataFrame
    table = generic_read_csv(f"Data/{csv_file}")

    # Get the table name from the CSV file name
    table_name = os.path.splitext(csv_file)[0] + "_raw"

    # Insert the data into the database
    table.to_sql(f"{table_name}", conn, if_exists="replace", index=False)

# Close the connection
conn.close()
# %%
