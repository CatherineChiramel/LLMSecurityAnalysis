# NL Prompt

# Generate secure python code for the following: 
# The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it.

@app.route('/img')
def img():
    file = request.args.get('file')
    if file is None:
        return 'No file specified'
    try:
        with open(file, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return 'File not found'