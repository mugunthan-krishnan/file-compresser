import os
import openpyxl
from zipfile import ZipFile
from django.conf import settings 

# Log File Data
def createLogFile(filenames, inputFilesSize, compressionSpeed):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    logData = [('FILENAME', 'COMPRESSION RATIO', 'COMPRESSION SPEED (BYTES/SECOND)')]
    for i in range(len(filenames)):
        original_size = inputFilesSize[filenames[i]]
        file_path = os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', filenames[i])
        compressed_size = os.path.getsize(file_path)
        compression_ratio = original_size / compressed_size
        compression_speed = compressionSpeed[i]
        logData.append((filenames[i],str(compression_ratio),str(compression_speed)))
    for row_data in logData:
        sheet.append(row_data)
    logFilePath = os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', 'logfile.xlsx')
    workbook.save(logFilePath)

def createZipFile(zipfilePath, filenames, zip_buffer):
    with ZipFile(zip_buffer, 'w') as zipObj:
        # Add multiple files to the zip
        for f in filenames:
            toBeZippedFileName = os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', f)
            zipObj.write(toBeZippedFileName, os.path.basename(toBeZippedFileName))
    zip_buffer.seek(0)
    return zip_buffer

def createFiles(filenames, contents):
    # Create the files in the tmp directory in Heroku Ephemeral Filesystem
    for i in range(len(filenames)):
        file_path = os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', filenames[i])
        with open(file_path, 'wb') as f:
            f.write(contents[i])