import io
import os
import zlib
from filecompressor.helpers.preProcessOps import *
from filecompressor.helpers.helperFunctions import *
from django.shortcuts import render
from django.http import HttpResponse

# Global Variables
filestreams = []
filenames = []
keys = []
contents=[]

def decompressPage(request):
    enabledwnld = False
    if request.method == "GET":
        empty_tmp_folder()
        filestreams.clear()
        filenames.clear()
    
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

        # Decompress the uploaded files when decompress button is clicked.
        if request.POST.get("decompress"):
            for f in range(len(filestreams)):
                decompressed_data = zlib.decompress(filestreams[f])
                key = fs.put(decompressed_data, filename=filenames[f])
                keys.append(key)
                contents.append(fs.get(key).read())

            createFiles(filenames, contents)
            enabledwnld = True

        # Download the decompressed files as a zip file when download file button is clicked.
        if request.POST.get("download"):
            enabledwnld = False
            zipfilePath =  os.path.join(settings.BASE_DIR,'filecompressor', 'tmp', 'decompressed.zip')
            zip_buffer = io.BytesIO()
            zip_buffer = createZipFile(zipfilePath, filenames, zip_buffer)
            filenames.clear()
            filestreams.clear()
            response = HttpResponse(zip_buffer, content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename="decompressed.zip"'
            return response
    
    return render(request,'decompress.html', {'enabledwnld':enabledwnld, 'filenames':filenames})