# NL Prompt

# Generate python code for the following: 
# The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it.

from flask import Flask, request

app = Flask(__name__)

@app.route('/img')
def img():
    file_name = request.args.get('file')
    try:
        with open('images/' + file_name, 'rb') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return 'File Not Found', 404

if __name__ == '__main__':
    app.run()
