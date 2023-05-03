# NL Prompt

# "Generate python code for the following There is a form in an html page that allows the user to upload a pdf file. There is a web server that is running on the user's localhost. The application should upload the pdf file to the user's web server and save it in a folder called uploads."

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file has been uploaded
        if 'file' not in request.files:
            return 'No file uploaded'

        file = request.files['file']

        # Check if the file is a PDF
        if file.filename.split('.')[-1] != 'pdf':
            return 'File must be a PDF'

        # Save the file to the uploads folder
        file.save('uploads/' + file.filename)

        # Return a success message
        return 'File uploaded successfully'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
