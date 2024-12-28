# coding: utf-8

# # Function



# import pandas as pd

def WriteDB(data, output_path, sep=',', filetype='CSV'):
    """
    Writes a DataFrame to a specified file format.

    Parameters:
        data (DataFrame): The DataFrame to write.
        output_path (str): The file path to write the data to.
        sep (str): The separator to use for CSV files (default is ',').
        filetype (str): The file format to write (options: 'CSV', 'XLSX', 'XML', 'JSON', 'Parquet').

    Returns:
        bool: True if the file is written successfully, False otherwise.
    """
    try:
        # Determine file type and write accordingly
        if filetype.upper() == 'CSV':
            data.to_csv(output_path, sep=sep, index=False)
        elif filetype.upper() == 'XLSX':
            data.to_excel(output_path, index=False)
        elif filetype.upper() == 'XML':
            data.to_xml(output_path, index=False)
        elif filetype.upper() == 'JSON':
            data.to_json(output_path, orient='records', indent=4)
        elif filetype.upper() == 'PARQUET':
            data.to_parquet(output_path, index=False)
        else:
            print("Unsupported file type. Please choose from 'CSV', 'XLSX', 'XML', 'JSON', or 'Parquet'.")
            return False
        print(f"File written successfully to {output_path}")
        return True
    except Exception as e:
        print("An error occurred while writing the file:", e)
        return False


# # Examples



# # Example DataFrame
# import pandas as pd

# # Sample data for the DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [24, 30, 22],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)


# ## CSV



# WriteDB(df, '../../../Datasets/Testing/test_csv.csv', sep=',', filetype='CSV')


# ## XLSX



# WriteDB(df, '../../../Datasets/Testing/test_xlsx.xlsx', sep=',', filetype='XLSX')


# ## PARQUET



# WriteDB(df, '../../../Datasets/Testing/test_parquet.parquet', sep=',', filetype='PARQUET')


# 
# ## JSON



# WriteDB(df, '../../../Datasets/Testing/test_json.json', sep=',', filetype='JSON')


# ## XML



# WriteDB(df, '../../../Datasets/Testing/test_xml.xml', sep=',', filetype='XML')

