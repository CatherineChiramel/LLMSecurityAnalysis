# NL Prompt

# "Generate python code for the following A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser."

from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/img/<string:name>')
def img(name):
    file_path = os.path.join('images', name)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File not found", 404
