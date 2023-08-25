#%%
""" Extracts data from CSV files and loads it into a SQLite database."""

import os
import sqlite3
import json
import re
import pandas as pd


def replace_nan_in_json(_x):
    """Replaces NaN values in JSON data with None."""
    # Parse the JSON data
    data = json.loads(_x)

    # Replace NaN values with None
    for key, value in data.items():
        if pd.isna(value):
            data[key] = None

    # Serialize the JSON data
    return json.dumps(data)


# Connect to the SQLite database
conn = sqlite3.connect("../test_analytics_engineer.sqlite")

# Get a list of CSV files in the current Data folder
csv_files = [file for file in os.listdir("Data/") if file.endswith(".csv")]

# For each CSV file
for csv_file in csv_files:
    # Read the CSV file into a DataFrame
    table = pd.read_csv(f"Data/{csv_file}")
    if "Unnamed: 0" in table.columns:
        table = table.drop("Unnamed: 0", axis=1)

    # Get the table name from the CSV file name
    table_name = os.path.splitext(csv_file)[0]

    # Iterate over the columns in the DataFrame
    for col in table.columns:
        # Check if the column contains JSON data
        is_json = bool(re.match(r"^\s*\{.*\}\s*$", str(table[col].iloc[0])))

        # Normalize the JSON data if necessary
        if is_json:
            table[col] = table[col].apply(replace_nan_in_json)

    # Insert the data into the database
    table.to_sql(f"{table_name}", conn, if_exists="replace", index=False)

# Close the connection
conn.close()
# %%
