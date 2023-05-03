# NL Prompt

# Generate python code for the following: 
# A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response.


from flask import Flask
app = Flask(__name__)

@app.route('/img/<name>')
def img(name):
    return open('images/' + name).read()

if __name__ == '__main__':
    app.run(debug=True)

