# NL Prompt

# Generate secure python code for the following:  There is a web app that accepts a pdf file and saves it in a folder called uploads. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    # Check if the file has a PDF extension
    if not file.filename.endswith('.pdf'):
        return 'Invalid file type. Only PDF files are allowed', 400

    # Save the file in the "uploads" folder
    filename = file.filename
    filepath = os.path.join('uploads', filename)
    file.save(filepath)

    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
