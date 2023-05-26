import pandas as pd
import glob
import os

file_paths = glob.glob('to_be_processed/*.csv')

for file_path in file_paths:
    df = pd.read_csv(file_path)

    # delete row 1
    df = df.iloc[1:]

    # delete 'id', 'logId', and 'chunkID' columns
    df = df.drop(columns=['id', 'logId', 'chunkID'], errors='ignore')

    # rename 'userID' to 'speaker' and 'transcriptText' to 'text'
    df = df.rename(columns={'userID': 'speaker', 'transcriptText': 'text'})

    # get the filename without the extension
    filename = os.path.basename(file_path).split('.')[0]

    # define the output file path
    output_file_path = f'processed/{filename}.xlsx'

    # save the modified DataFrame to an Excel file
    df.to_excel(output_file_path, index=False)