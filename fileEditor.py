import pandas as pd
import glob
import os

# Get all CSV file paths in the 'to_be_processed/' directory
file_paths = glob.glob('to_be_processed/*.csv')

for file_path in file_paths:
    # Load the data, indicating no header
    df = pd.read_csv(file_path, skiprows=1)  # This will skip the first row

    # Delete 'id', 'logId', and 'chunkId' columns
    df = df.drop(columns=['id', 'logId', 'chunkId'], errors='ignore')

    # Rename 'userId' to 'speaker' and 'transcriptText' to 'text'
    df = df.rename(columns={'userId': 'speaker', 'transcriptText': 'text'})

    # Get the filename without the extension
    filename = os.path.basename(file_path).split('.')[0]

    # Define the output file path
    output_file_path = f'processed/{filename}.xlsx'

    # Save the modified DataFrame to an Excel file
    df.to_excel(output_file_path, index=False)

    # Delete the original file
    os.remove(file_path)
