# coding: utf-8

# # Function



import pandas as pd
import numpy as np

def ReadDB(intake, sep=','):
    """
    Reads a CSV, XLSX, XML, JSON, or Parquet file from a specified URL or file path.

    Parameters:
        intake (str): The URL or local file path of the file.
        sep (str): The separator used in CSV files (default is ',').

    Returns:
        DataFrame: The loaded data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        # Determine file type based on extension and read accordingly
        if intake.endswith('.csv'):
            data = pd.read_csv(intake, sep=sep)
        elif intake.endswith('.xlsx'):
            data = pd.read_excel(intake)
        elif intake.endswith('.xml'):
            data = pd.read_xml(intake)
        elif intake.endswith('.json'):
            data = pd.read_json(intake)
        elif intake.endswith('.parquet'):
            data = pd.read_parquet(intake)
        else:
            print("Unsupported file type. Only .csv, .xlsx, .xml, .json, and .parquet files are supported.")
            return None
        return data
    except Exception as e:
        print("An error occurred:", e)
        return None


# # Examples

# ## CSV



ReadDB(intake = r'../../../Datasets/Testing/test_csv.csv', sep=',')


# ## XLSX



ReadDB(intake = r'../../../Datasets/Testing/test_xlsx.xlsx')


# ## PARQUET



ReadDB(intake = r'../../../Datasets/Testing/test_parquet.parquet')


# ## JSON



ReadDB(intake = r'../../../Datasets/Testing/test_json.json')


# ## XML



ReadDB(intake = r'../../../Datasets/Testing/test_xml.xml')

