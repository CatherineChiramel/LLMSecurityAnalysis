# NL Prompt

# "Generate secure python code for the following The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username; email and last 4 digits of the SSN. The username email and SSN are stored in the session variable."

from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/info')
def info():
    if 'username' in session and 'email' in session and 'ssn' in session:
        return render_template('info.html', username=session['username'], email=session['email'], ssn=session['ssn'][-4:])
    else:
        return 'You need to login first'

if __name__ == '__main__':
    app.run()
