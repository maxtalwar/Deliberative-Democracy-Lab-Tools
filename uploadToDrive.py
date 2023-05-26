from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import os
import glob
import csv
from xlsxwriter.workbook import Workbook
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
upload_file_list = []

for csvfile in glob.glob(os.path.join('./processed', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    upload_file_list.append(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()

for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1zlWyYfzWGGp7_l97s6QKSbOeMFVeIF3O'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.