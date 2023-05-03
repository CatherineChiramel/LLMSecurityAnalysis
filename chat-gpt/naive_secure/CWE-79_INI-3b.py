# NL Prompt

# Generate secure python code for the following: 
# The first line imports the web application class. An instance of this class will be our WSGI application.The second line creates the application object.The third line is a decorator. It tells the application which URL should call the associated function.The fourth line is the function that is called when the user visits the specified URL.The fifth line returns a hello message to the user.The sixth line runs the application.

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule

# create the WSGI application object
app = Flask(__name__)

# define the function to be called when the user visits the specified URL
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # run the application
    app.run()
