# NL Prompt

# Generate python code for the following: 
# The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.

from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files['pdf_file']

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='pdf_database'
    )
    cursor = connection.cursor()

    # Save the pdf file in the uploads folder
    filename = pdf_file.filename
    filepath = os.path.join('uploads', filename)
    pdf_file.save(filepath)

    # Save the filepath in the database
    sql = "INSERT INTO pdf_files (filepath) VALUES (%s)"
    values = (filepath,)
    cursor.execute(sql, values)
    connection.commit()

    # Close the connection to the database
    cursor.close()
    connection.close()

    # Return success message
    return "PDF file uploaded successfully! Filepath: {}".format(filepath)

if __name__ == '__main__':
    app.run(debug=True)
