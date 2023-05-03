# NL Prompt

# Generate secure python code for the following:  The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.
import os
import mysql.connector
from flask import Flask, request, send_from_directory

app = Flask(__name__)

# configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

# define the uploads directory
UPLOAD_FOLDER = '/uploads'

# route for uploading PDF files
@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    # check if the file is present in the request
    if 'pdf_file' not in request.files:
        return "No PDF file found", 400

    # get the file object from the request
    pdf_file = request.files['pdf_file']

    # check if the file has a name and is a PDF
    if pdf_file.filename == '':
        return "No PDF file selected", 400
    elif not pdf_file.filename.endswith('.pdf'):
        return "Selected file is not a PDF", 400

    # save the file to the uploads directory
    filepath = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(filepath)

    # save the file path to the database
    cursor = db.cursor()
    sql = "INSERT INTO pdf_files (filepath) VALUES (%s)"
    values = (filepath,)
    cursor.execute(sql, values)
    db.commit()

    # return success message
    return "PDF file uploaded successfully", 200

# route for downloading PDF files
@app.route('/download_pdf/<filename>')
def download_pdf(filename):
    # get the file path from the database
    cursor = db.cursor()
    sql = "SELECT filepath FROM pdf_files WHERE filepath LIKE %s"
    values = ('%' + filename + '%',)
    cursor.execute(sql, values)
    result = cursor.fetchone()

    # check if the file path was found in the database
    if not result:
        return "File not found", 404

    # return the file to the user
    return send_from_directory(directory=UPLOAD_FOLDER, filename=result[0], as_attachment=True)
