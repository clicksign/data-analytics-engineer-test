#%%
"""Extracts data from CSV files and loads it into the SQLite database."""
import os
import sqlite3
import json
import re
import pandas as pd


def replace_nan_in_json(data):
    """Replaces NaN values in JSON data with None."""
    return json.dumps(
        {
            key: value if pd.notna(value) else None
            for key, value in json.loads(data).items()
        }
    )


def read_csv_and_clean(file_path):
    """Reads a CSV file, drops 'Unnamed: 0' column if present,
    and normalizes JSON data if the ***first value in the column*** is json like."""
    table = pd.read_csv(file_path)
    if "Unnamed: 0" in table.columns:
        table = table.drop("Unnamed: 0", axis=1)

    for col in table.columns:
        if is_json_data(table[col].iloc[0]):
            table[col] = table[col].apply(replace_nan_in_json)

    return table


def is_json_data(value):
    """Checks if a given value is in JSON format."""
    return bool(re.match(r"^\s*\{.*\}\s*$", str(value)))


def insert_into_database(table, table_name, conn):
    """Inserts a DataFrame into the SQLite database."""
    table.to_sql(table_name, conn, if_exists="replace", index=False)


def main():
    """Reads CSV files in the Data folder, cleans the data, and inserts it into
    the SQLite database."""
    # Connect to the SQLite database
    conn = sqlite3.connect("../test_analytics_engineer.sqlite")

    # Get a list of CSV files in the current Data folder
    csv_files = [file for file in os.listdir("Data/") if file.endswith(".csv")]

    for csv_file in csv_files:
        table_name = os.path.splitext(csv_file)[0]
        file_path = os.path.join("Data", csv_file)

        table = read_csv_and_clean(file_path)
        insert_into_database(table, table_name, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()

# %%
