import pandas as pd
import glob
import os
from googletrans import Translator


translator = Translator()
# Get all CSV file paths in the 'to_be_processed/' directory
file_paths = glob.glob('to_be_processed/*.csv')


for file_path in file_paths:
    # Get the filename without the extension
    filename = os.path.basename(file_path).split('.')[0]

    # Load the data, indicating no header
    df = pd.read_csv(file_path, skiprows=1)  # This will skip the first row

    #translate the transcript text if necessary
    language = filename[14:16]
    if language != "en":
        for i in range(len(df.index)):
            df.loc[i,'transcriptText'] = translator.translate(df.loc[i,'transcriptText'], src=language).text

    # Delete 'id', 'logId', and 'chunkId' columns
    df = df.drop(columns=['id', 'logId', 'chunkId'], errors='ignore')

    # Rename 'userId' to 'speaker' and 'transcriptText' to 'text'
    df = df.rename(columns={'userId': 'speaker', 'transcriptText': 'text'})

    # Define the output file path
    output_file_path = f'processed/{filename}.xlsx'

    writer = pd.ExcelWriter(output_file_path, engine = 'xlsxwriter')

    # Save the modified DataFrame to an Excel file
    df.to_excel(writer, sheet_name="Transcript", index=False)

    #Init new Excel tab
    dfNewTab = pd.read_csv("proposal.csv", skiprows=1)

    #Save new Excel tab
    dfNewTab.to_excel(writer, sheet_name="proposal", index=False)

    #Close writer
    writer.close()

    # Delete the original file
    # os.remove(file_path)
