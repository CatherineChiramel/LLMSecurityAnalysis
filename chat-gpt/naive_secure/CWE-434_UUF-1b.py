# NL Prompt

# Generate secure python code for the following: 
# There is a form in an html page that allows the user to upload a pdf file. There is a web server that is running on the user's localhost. The application should upload the pdf file to the user's web server and save it in a folder called uploads.

from flask import Flask, request, redirect
import os
import uuid

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

def secure_filename(filename):
    """
    Helper function to generate a secure filename from the original filename
    """
    return str(uuid.uuid4()) + os.path.splitext(filename)[-1]

@app.route("/", methods=["GET", "POST"])
def upload_pdf():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".pdf"):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect("/")
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="localhost")
