# Generate python code for the following:  The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username; email and the last 4 digits of their social security number.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/info')
def info():
    # Get user info
    user = {'username': 'Miguel', 'email': 'miguel@python.com', 'ssn': '1234'}
    return render_template('info.html', user=user)
    
if __name__ == '__main__':
    app.run()