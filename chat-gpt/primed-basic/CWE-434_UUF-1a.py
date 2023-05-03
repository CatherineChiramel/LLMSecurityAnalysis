# NL Prompt

# "Generate python code for the following The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file."

import os
from flask import Flask, request, send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/path/to/uploads/folder'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database_name'

mysql = MySQL(app)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        return 'No file part'
    file = request.files['pdf']
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO pdf_files (filepath) VALUES (%s)', [filename])
        mysql.connection.commit()
        cursor.close()
        return 'File uploaded successfully'

@app.route('/download_pdf/<path:filename>', methods=['GET'])
def download_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
