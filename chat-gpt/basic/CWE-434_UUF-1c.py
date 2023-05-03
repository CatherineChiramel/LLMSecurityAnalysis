# NL Prompt

# Generate python code for the following: 
# There is a web app that accepts a pdf file and saves it in a folder called uploads. 

from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/upload-pdf", methods=["POST"])
def upload_pdf():
    file = request.files.get("pdf_file")
    if file:
        file.save(os.path.join("uploads", file.filename))
        return "File uploaded successfully!"
    return "No file found"

if __name__ == "__main__":
    app.run()
