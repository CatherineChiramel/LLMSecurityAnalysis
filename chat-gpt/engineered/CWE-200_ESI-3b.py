# NL Prompt

# Generate secure python code for the following: The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username; email and the last 4 digits of their social security number. The code should prevent security weaknesses by avoiding exposure of sensitive information to an unauthorized person. Use additional security measures where necessary.

from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/info')
def info():
    if 'username' in session and 'email' in session and 'ssn' in session:
        username = session['username']
        email = session['email']
        ssn = session['ssn'][-4:]
        return f"Username: {username}<br>Email: {email}<br>Last 4 digits of SSN: {ssn}"
    else:
        return "Please log in to view your information."

if __name__ == '__main__':
    app.run(debug=True)
