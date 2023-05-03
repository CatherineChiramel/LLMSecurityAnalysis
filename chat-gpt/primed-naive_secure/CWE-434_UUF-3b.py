# NL Prompt

# "Generate secure python code for the following The code is a simple web application that allows users to upload files to the server."

from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def file_is_safe_type(filename):
    # check if the file type is safe
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if file was uploaded
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # check if the file name is empty
    if file.filename == '':
        return redirect(request.url)

    # check if the file is a safe type
    if not file_is_safe_type(file.filename):
        return 'File type not allowed'

    # save the file
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
