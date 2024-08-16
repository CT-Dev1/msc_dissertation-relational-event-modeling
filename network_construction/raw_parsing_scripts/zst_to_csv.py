import zstandard as zstd
import io
import json
import pandas as pd
import csv
import os
import glob

def convert_zst_to_csv(file_name, output_csv_file):
    with open(file_name, 'rb') as fh, open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
        stream_reader = dctx.stream_reader(fh)
        text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
        
        csv_writer = csv.writer(csvfile)
        
        # Initialize header variable outside the loop
        header = None
        
        # Iterate over each JSON object to determine headers dynamically
        for line in text_stream:
            obj = json.loads(line)
            
            # Extract keys if not already done
            if header is None:
                header = obj.keys()
                csv_writer.writerow(header)
            
            # Write values for each JSON object, handling missing keys gracefully
            csv_writer.writerow([obj.get(key, '') for key in header])

# Specify the folder path
input_folder = "/path/to/zst/folder"
#Specify output file prefix
output_file = "full_submissions_2021"
i = 1 # counter for month - modify to match first month of data - 1

# List all files in the specified folder
for file_name in os.listdir(input_folder):
    i += 1
    # Full path of the file
    file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        print(file_path) # Print current file
        output = output_file + "_" + str(i) +".csv"
        convert_zst_to_csv(file_path,output)