import sqlite3
import pandas as pd

## Functions

def create_sqlite_connection(database):
    """
    Connect to the database (creates a new database if it doesn't exist)
    ---
    database - database name
    """
    # creates connection
    conn = sqlite3.connect(database)
    # sets cursor
    c = conn.cursor()
    return conn, c

def create_sqlite_table(table_name, conn, schema):
    """
    Create a table in SQLite
    ---
    table_name - name of the table to be created
    conn - connection to database
    schema - schema name
    """
    # get file location and name
    file_name = f'Data/{table_name}.csv'
    # read csv file as pandas DataFrame
    df = pd.read_csv(file_name)
    # sends Dataframe as table to specified schema 
    df.to_sql(table_name, conn, schema, 'replace', False)


## Parameters

database = 'test_analytics_engineer.db'
schema =  'test_analytics_engineer'
table_names = ['Country', 
               'League', 
               'Match', 
               'Player_Attributes', 
               'Player', 
               'Team_Attributes', 
               'Team']


# Execution
conn, c = create_sqlite_connection(database)
for name in table_names:
    create_sqlite_table(name, conn, schema)