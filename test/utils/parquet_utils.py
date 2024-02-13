from datetime import datetime
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from resources.testdata.schemas import schema1


def create_parquet_file(data=schema1.data, schema=schema1.schema, parquet_file_name=None):
    df = pd.DataFrame(data, columns=schema.names)
    table = pa.Table.from_pandas(df, schema=schema)
    parquet_file = 'resources/testdata/parquet_files/' + parquet_file_name
    if os.path.exists(parquet_file):
        os.remove(parquet_file)  # Remove the existing file if it exists
    pq.write_table(table, parquet_file)
    print(f"parquet file: {parquet_file_name} create successfully")


# def create_parquet_file(data, schema, parquet_file):
#     if os.path.exists(parquet_file):
#         os.remove(parquet_file)  # Remove the existing file if it exists
#
#     table = pa.Table.from_pandas(data, schema=schema)
#     pq.write_table(table, parquet_file)

def load_parquet_as_dataframe(parquet_path):
    parquet_table = pq.read_table(parquet_path)
    parquet_df = parquet_table.to_pandas()
    return parquet_df


def get_future_date_rows(parquet_path, date_column_name):
    # Load the Parquet file into a DataFrame
    parquet_table = pq.read_table(parquet_path)
    parquet_df = parquet_table.to_pandas()

    # Convert the date column to datetime if it's not already
    parquet_df[date_column_name] = pd.to_datetime(parquet_df[date_column_name])

    # Define the current date
    current_date = datetime.now()

    # Filter rows with dates greater than the current date
    future_date_rows = parquet_df[parquet_df[date_column_name] > current_date]

    return future_date_rows


def get_duplicate_rows(parquet_path):
    # Load the Parquet file into a DataFrame
    parquet_table = pq.read_table(parquet_path)
    parquet_df = parquet_table.to_pandas()

    # Identify and retrieve duplicate rows based on all columns
    duplicate_rows = parquet_df[parquet_df.duplicated(keep=False)]

    return duplicate_rows


def remove_future_dates_and_duplicates(parquet_path, date_column_name):
    # Load the Parquet file into a DataFrame
    parquet_table = pq.read_table(parquet_path)
    parquet_df = parquet_table.to_pandas()

    # Convert the date column to datetime if it's not already
    parquet_df[date_column_name] = pd.to_datetime(parquet_df[date_column_name])

    # Define the current date
    current_date = datetime.now()

    # Filter rows with dates greater than the current date
    future_date_rows = parquet_df[parquet_df[date_column_name] > current_date]

    # Identify and retrieve duplicate rows based on all columns
    duplicate_rows = parquet_df[parquet_df.duplicated(keep=False)]

    # Combine filters to remove both future dates and duplicates
    filtered_df = parquet_df[
        ~parquet_df.index.isin(future_date_rows.index) & ~parquet_df.index.isin(duplicate_rows.index)]

    return filtered_df


def remove_duplicates_and_fetch_df(parquet_path):
    # Load the Parquet file into a DataFrame
    parquet_table = pq.read_table(parquet_path)
    parquet_df = parquet_table.to_pandas()

    # Identify and remove duplicate rows based on all columns
    deduplicated_df = parquet_df.drop_duplicates()

    # Return the filtered DataFrame
    return deduplicated_df
