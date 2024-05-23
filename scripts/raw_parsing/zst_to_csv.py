import zstandard as zstd
import io
import json
import pandas as pd
import csv
import os
import glob

# Example: convert folder of zst compressed files to single csv with:
# python zst_to_csv.py /path/to/input_folder /path/to/output_folder/combined.csv

def convert_zst_to_csv(file_name, csv_writer, header_written):
    ''' Modified Function from u/ramnamsatyahai to convert single zst file to single csv file'''

    with open(file_name, 'rb') as fh:
        dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
        stream_reader = dctx.stream_reader(fh)
        text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
        
        # Initialize header variable outside the loop
        header = None
        
        # Iterate over each JSON object to determine headers dynamically
        for line in text_stream:
            obj = json.loads(line.strip())
            
            if not obj:  # skip empty lines
                continue
            
            # Extract keys if not already done
            if not header_written:
                header = obj.keys()
                csv_writer.writerow(header)
                header_written = True
            
            # Write values for each JSON object, handling missing keys gracefully
            csv_writer.writerow([obj.get(key, '') for key in header])
    
    return header_written

def process_zst_files(input_folder, output_file):
    '''Function to process entire zst file folder and write to single csv file'''
    # Get all .zst files in the input folder
    zst_files = glob.glob(os.path.join(input_folder, '*.zst'))
    
    header_written = False
    
    # Open the output CSV file once
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Iterate over each .zst file and append its contents to the single CSV file
        for zst_file in zst_files:
            header_written = convert_zst_to_csv(zst_file, csv_writer, header_written)

# Example usage
# input_folder = '/path/to/input_folder'
# output_file = '/path/to/output_folder/combined.csv'
# process_zst_files(input_folder, output_file)