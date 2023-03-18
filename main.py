import pandas as pd
from sqlalchemy import create_engine
import pyodbc

# Extract data from CSV
def extract_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# Transform the data into a DataFrame
def transform_data(data):
    df = pd.DataFrame(data)
    return df

# Load the data into the Azure SQL Database
def load_data_to_azure(df, connection_string, table_name):
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def main():
    # Replace these values with your own CSV file path and Azure SQL Database connection string
    csv_file_path = 'your_csv_file.csv'
    azure_connection_string = 'mssql+pyodbc://username:password@server.database.windows.net:1433/database_name?driver=ODBC+Driver+17+for+SQL+Server'

    # The destination table in the Azure SQL Database
    table_name = 'destination_table'

    # Extract data from the CSV
    raw_data = extract_data_from_csv(csv_file_path)

    # Transform the data into a DataFrame
    dataframe = transform_data(raw_data)

    # Load the data into the Azure SQL Database
    load_data_to_azure(dataframe, azure_connection_string, table_name)

if __name__ == '__main__':
    main()
