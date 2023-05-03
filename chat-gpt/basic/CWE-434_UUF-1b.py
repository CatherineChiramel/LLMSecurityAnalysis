# NL Prompt

# Generate python code for the following: 
# There is a form in an html page that allows the user to upload a pdf file. There is a web server that is running on the user's localhost. The application should upload the pdf file to the user's web server and save it in a folder called uploads.

from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        pdf_file = request.files['pdf']
        if pdf_file:
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename))
            return redirect(url_for('uploaded_file',
                                    filename=pdf_file.filename))
    return '''
    <!doctype html>
    <title>Upload new PDF</title>
    <h1>Upload a new PDF</h1>
    <form action="" method=post enctype=multipart/form-data>
      <input type=file name=pdf>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return '''
    <h1>File uploaded</h1>
    <p>The file has been saved as {} in the uploads folder.</p>
    '''.format(filename)

if __name__ == '__main__':
    app.run()
