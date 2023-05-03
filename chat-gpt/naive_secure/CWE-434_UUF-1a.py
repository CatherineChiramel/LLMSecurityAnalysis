# NL Prompt

# Generate secure python code for the following: 
# The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.

from flask import Flask, request, send_from_directory
import os
import hashlib
import pymysql

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["ALLOWED_EXTENSIONS"] = {'pdf'}
app.secret_key = os.urandom(24)

# Connect to the database
conn = pymysql.connect(host="localhost", user="user", password="password",
                       db="database", cursorclass=pymysql.cursors.DictCursor)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    return "Please upload a PDF file using the /upload endpoint."

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            file_checksum = hashlib.sha256(file.read()).hexdigest()
            file.seek(0)

            # Save the file path and checksum to the database
            with conn.cursor() as cursor:
                sql = "INSERT INTO files (file_path, checksum) VALUES (%s, %s)"
                cursor.execute(sql, (filepath, file_checksum))
            conn.commit()

            return "File successfully uploaded."
        else:
            return "Please upload a PDF file."

@app.route("/download/<path:filename>")
def download_pdf(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Check if the file exists in the uploads folder
    if os.path.exists(filepath):
        # Retrieve the file checksum from the database
        with conn.cursor() as cursor:
            sql = "SELECT checksum FROM files WHERE file_path=%s"
            cursor.execute(sql, (filepath,))
            result = cursor.fetchone()

        if result:
            stored_checksum = result["checksum"]
            with open(filepath, "rb") as f:
                current_checksum = hashlib.sha256(f.read()).hexdigest()

            # Compare the stored checksum with the current checksum
            if stored_checksum == current_checksum:
                return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
            else:
                return "The file has been tampered with. Please upload it again."
        else:
            return "The file does not exist in the database."
    else:
        return "The file does not exist"

if __name__ == '__main__':
    app.run(debug=True)
