import sqlite3
import pandas as pd

## Functions

# Connect to the database (creates a new database if it doesn't exist)
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

def column_selection(table_name):
    """
    Gets JSON keys from JSON column
    ---
    table_name - table to get JSON column's keys
    """
    # gets keys values to be used as column names
    column_names = pd.read_sql(f'''
                        SELECT DISTINCT json_each.key 
                        FROM {table_name}, 
                               json_each({table_name}) 
                        WHERE json_valid({table_name});
                            ''', con=conn)
    return column_names

def select_columns(column_names):
    """
    Gets SELECT SQL statement to transform JSON column 
    into multiple columns
    ---
    column_names - JSON key values to be used as column names
    """
    # set empty list
    column_list = list()
    # for each key:
    for col_name in column_names['key']:
        # append to list SQL statement to extract values from JSON column to new column
        column_list.append(f"json_extract({table_name}, '$.{col_name}') AS {col_name}")
    # append all strings
    columns_string = '\n,'.join(column_list)
    return columns_string

def create_table_sql_query(columns_string):
    """
    Constructs CREATE statement for new table with "_Modified" suffix
    ---
    columns_string - SELECT statement for JSON keys as columns 
    """
    # concatenate all strings necessary
    query_string = f"CREATE TABLE {table_name}_Modified AS \nSELECT "+columns_string+  f'''\nFROM {table_name}
    WHERE json_valid({table_name});'''
    return query_string

## Parameters

database = 'test_analytics_engineer.db'
# table_name = "Player_Attributes"
table_name = "Team_Attributes"

## Execution

conn, c = create_sqlite_connection(database)
column_names = column_selection(table_name)
selected_columns = select_columns(column_names)
sql_query_statement = create_table_sql_query(selected_columns)

print(sql_query_statement)    