import pandas as pd
from get_laureate_data import fetch_laureates
import snowflake.connector 
from snowflake.connector.pandas_tools import write_pandas
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

snowflake_config = config['Snowflake']

def add_to_snowflake_db():
    con = snowflake.connector.connect(
        user = snowflake_config['user'],
        password = snowflake_config['password'],
        account = snowflake_config['account'],
    )

    # Execute the nobelSnowflake SQL code to create a the desired DB objects
    with open('nobelSnowflake.sql', 'r') as file:
        sql_commands = file.read()

    sql_command_list = sql_commands.strip().split(';')

    for command in sql_command_list:
        con.cursor().execute(command)

    success, n_chunks, n_rows, _ = write_pandas(
        conn = con,
        df = fetch_laureates(),
        table_name = "PRIZE_WINNERS",
        schema = "NOBEL_CLEANED_DATA",
        database = "NOBEL_PRIZES"
    )

    print('Table successfully written to Snowflake')

if __name__ == '__main__':
    add_to_snowflake_db()