# NL Prompt

# "Generate python code for the following The code is a simple web application that allows users to upload files to the server."

from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the file upload form
@app.route('/')
def index():
    return render_template('upload.html')

# Route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file selected'

    file = request.files['file']

    # Check if the file is allowed
    if not file_is_safe_type(file.filename):
        return 'File type not allowed'

    # Save the file to the uploads directory
    file.save('uploads/' + file.filename)

    return 'File uploaded successfully'

# Function to check if the file type is allowed
def file_is_safe_type(filename):
    # Add your code to check the file type here
    return True

if __name__ == '__main__':
    app.run(debug=True)
