# NL Prompt

# "Generate python code for the following The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username; email and ssn of the user. The username email and ssn are stored in the session variable."

from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/info')
def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    if not all([username, email, ssn]):
        return "Error: missing user information"
    # Hash the SSN before displaying it to the user
    ssn_hash = hashlib.sha256(ssn.encode('utf-8')).hexdigest()[-4:]
    return f"Username: {username}<br>Email: {email}<br>SSN: XXX-XX-{ssn_hash}"
