import io
import os
import zlib
import time

from filecompressor.helpers.preProcessOps import empty_tmp_folder, preProcessOps
from filecompressor.helpers.helperFunctions import createFiles, createLogFile, createZipFile
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Global Variables
filestreams = []
filenames = []
foldernames = []
inputFilesSize = {}
keys = []
contents=[]
compressionSpeed = []

def compressPage(request):
    enabledwnld = False
    # Clear filenames, filestreams fpr every run.
    if request.method == "GET":
        empty_tmp_folder()
        filestreams.clear()
        filenames.clear()
        inputFilesSize.clear()
    
    if request.method == "POST":
        # Run pre processing steps for database.
        fs = preProcessOps()
        # Upload a file and its metadata.
        if request.POST.get("upload"):
            uploaded_files = request.FILES.getlist('file')
            for eachFile in uploaded_files:
                if eachFile.name and eachFile.name not in filenames:
                    data = eachFile.read()
                    filestreams.append(data)
                    filenames.append(eachFile.name)
                    inputFileSize = {eachFile.name:len(data)}
                    inputFilesSize.update(inputFileSize)

        # Compress the uploaded files when compress button is clicked.
        if request.POST.get("compress"):
            for f in range(len(filestreams)):
                start_time = time.time()
                compressed_data = zlib.compress(filestreams[f])
                end_time = time.time()
                if (end_time - start_time) <= 0.0:
                    compressionSpeed.append(len(compressed_data))
                else:
                    compressionSpeed.append(len(compressed_data) / (end_time - start_time))
                key = fs.put(compressed_data, filename=filenames[f])
                keys.append(key)
                contents.append(fs.get(key).read())
            
            createFiles(filenames, contents)
            createLogFile(filenames, inputFilesSize, compressionSpeed)
            enabledwnld = True

        # Download the compressed files as a zip file when download file button is clicked.
        if request.POST.get("download"):
            enabledwnld = False
            filestreams.clear()
            zipfilePath =  os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', 'compressed.zip')
            zip_buffer = io.BytesIO()
            zip_buffer = createZipFile(zipfilePath, filenames, zip_buffer)
            filenames.clear()
            response = HttpResponse(zip_buffer, content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename="compressed.zip"'
            return response
        # Download the log file as a txt file when download log file button is clicked.
        if request.POST.get('downloadlogfile'):
            logFilePath = os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', 'logfile.xlsx')
            response = HttpResponse(open(logFilePath), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'attachment; filename="logfile.xlsx"'
            return response

    return render(request,'compress.html', {'enabledwnld':enabledwnld, 'filenames':filenames})