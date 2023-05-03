# NL Prompt

# "Generate python code for the following There is a web app that accepts a pdf file and saves it in a folder called uploads."

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the request contains a file
    if 'file' not in request.files:
        return 'No file provided'
    
    file = request.files['file']
    # Check if the file is a PDF
    if file.mimetype != 'application/pdf':
        return 'File is not a PDF'
    
    # Save the file to the uploads folder
    file.save('uploads/' + file.filename)
    
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
