import pandas as pd
import glob
import os

# Step 0: Get all CSV file paths in the 'to_be_processed/' directory
file_paths = glob.glob('to_be_processed/*.csv')

for file_path in file_paths:
    # Load the data
    df = pd.read_csv(file_path)

    # Step 1: Delete row 1
    df = df.iloc[1:]

    # Step 2: Delete 'id', 'logId', and 'chunkID' columns
    df = df.drop(columns=['id', 'logId', 'chunkID'], errors='ignore')

    # Step 3: Rename 'userID' to 'speaker' and 'transcriptText' to 'text'
    df = df.rename(columns={'userID': 'speaker', 'transcriptText': 'text'})

    # Get the filename without the extension
    filename = os.path.basename(file_path).split('.')[0]

    # Define the output file path
    output_file_path = f'processed/{filename}.xlsx'

    # Save the modified DataFrame to an Excel file
    df.to_excel(output_file_path, index=False)
    
    # Delete the original file
    os.remove(file_path)
