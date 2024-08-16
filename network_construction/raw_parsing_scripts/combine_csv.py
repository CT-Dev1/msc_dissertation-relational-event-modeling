import pandas as pd
import glob
import os

def combine_csv_files(input_folder, output_file):
    # Get all CSV files in the input folder
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    
    # Check if there are any CSV files in the folder
    if not csv_files:
        raise ValueError("No CSV files found in the specified folder.")
    
    # Initialize an empty list to hold DataFrames
    df_list = []

    # Read each CSV file and append it to the list
    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Write the combined DataFrame to the output CSV file
    combined_df.to_csv(output_file, index=False)

# Example usage
input_folder = "/path/to/input/zst/folder"
output_file = "path/to/(insert_file_name).csv"
combine_csv_files(input_folder, output_file)
