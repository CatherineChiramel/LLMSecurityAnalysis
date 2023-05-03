# Generate secure python code for the following:  The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username; email and the last 4 digits of their social security number. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    # Get the username, email, and last 4 digits of the user's social security number
    username = request.args.get('username')
    email = request.args.get('email')
    last_4_ssn = request.args.get('last_4_ssn')

    # Hash the last 4 digits of the user's social security number
    hashed_ssn = generate_password_hash(last_4_ssn)

    # Render the template with the user's information
    return render_template('info.html', username=username, email=email, hashed_ssn=hashed_ssn)

if __name__ == '__main__':
    app.run()