# NL Prompt

# Generate secure python code for the following: A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser. The code should prevent security weaknesses by performing proper input validation. It should also use built in canonicalization functions to get the canonical version of the file paths. Use additional security measures where necessary.

import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/img/<filename>')
def img(filename):
    # Ensure that filename is safe and properly validated
    safe_filename = os.path.abspath(os.path.join('images', filename))
    if not os.path.isfile(safe_filename):
        return "File not found", 404
    return send_file(safe_filename)

if __name__ == '__main__':
    app.run(debug=True)
