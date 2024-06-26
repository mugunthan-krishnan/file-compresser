# File Compressor Utility

Application Name: File Compressor

Developed By:

Mugunthan Krishnan

---

**About this file**

The purpose of this file is to provide overview, setup instructions and background information of the project.

---

**Technical Specifications**
1. Programming Languages: Python3, HTML, Bootstrap5

2. Web Framework: Django

3. Database: MongoDB


**How to run the application locally?**

1. The django application requires multiple libraries to be installed.

2. Install the libraries using the following command by navigating to the parent folder of the code. From either Visual Studio Code terminal or the command prompt, run the following commands.

**Install python > 3.10 version to your machine**

**pip install -r requirements.txt**

The above command installs the necessary libraries to run the flask application in your local machine.

Navigate to the folder named 'file-compressor-django' in the terminal and then run the below command to start the application.

**python manage.py runserver**

3. The django app starts and a localhost link is provided.

Navigate to localhost:8000 in your browser to open the application.

---

Please follow the below steps to use the application.

a. **Home Page:** The home page contains two routes - Compress and Decompress. It also provides an Info button to download the README file of the application. When the ‘Compress’ button is clicked, the application redirects to the compression page. When the ‘Decompress’ button is clicked, the application redirects to the decompression page.

b. **Compression:** The compress page consists of a file upload. Multiple files can be uploaded at the same time to compress together.

**Steps:**

1. Click on ‘Choose File’ and select a file from your local machine.

2. Click on ‘Upload’ to upload the file. After the file is uploaded, the list of files to be compressed is displayed and the Compress button is visible.

3. Follow Step-2 again to upload another file or click on Compress to compress the file(s) uploaded.

4. Click on Compress to compress the uploaded files.

5. ‘Download ZIP File’ and ‘Download Log File’ buttons appear on the screen. After the compression is successful, these buttons appear.

6. Click on ‘Download ZIP File’. The compressed file(s) are downloaded as a zip file to the default downloads directory in your local machine. The zip file name is ‘compressed.zip’.

**Note**: The 'compressed.zip' file contains the compressed files. Extracting the zip file will give the compressed files. Upload these files to decompress using the Decompression page. Opening these files would lead to error, since these files are compressed which are not viewable until decompression.

7. Click on ‘Download Log File’. A log file is downloaded to the local machine. The log file contains the filenames and speed and compression ratio for each of the files compressed. The log file is an xlsx workbook.

c. **Decompression:** The decompress page consists of a file upload. Multiple files can be uploaded at the same time to decompress together. To successfully decompress the files, upload the files that were compressed by this application.

**Note:** The upload functionality accepts multiple files at a time. But DONOT upload the zip file directly.

**Steps:**

1. Click on ‘Choose File’ and select a file from your local machine.

2. Click on ‘Upload’ to upload the file. After the file is uploaded, the list of files to be decompressed is displayed and the Decompress button is visible.

3. Follow Step-2 again to upload another file or click on Decompress to compress the file(s) uploaded.

4. Click on Decompress to decompress the uploaded files.

5. ‘Download ZIP File’ button appears on the screen. After the decompression is successful, the button appears.

6. Click on ‘Download ZIP File’. The decompressed file(s) are downloaded as a zip file to the default downloads directory in your local machine. The zip file name is ‘decompressed.zip’.

**Note**: The 'decompressed.zip' file contains the decompressed original files. Extracting the zip file will give the decompressed files. These files are viewable.
