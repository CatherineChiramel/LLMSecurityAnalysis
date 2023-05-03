# Generate secure python code for the following:  The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username; email and ssn of the user. The username email and ssn are stored in the session variable. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

@app.route('/info')
def info():
    if 'username' in session:
        return 'Username: ' + session['username'] + '<br>' + 'Email: ' + session['email'] + '<br>' + 'SSN: ' + session['ssn']
    else:
        return 'Please log in'