import zstandard as zstd
import io
import json
import pandas as pd
import csv


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


#replace newscomments with your dataset name 
convert_zst_to_csv("news_comments.zst", "newscomments.csv")