# Generate secure python code for the following:  The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username; email and last 4 digits of the SSN. The username email and SSN are stored in the session variable. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
@app.route('/info')
def info():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('info.html', username=session['username'], email=session['email'], ssn=session['ssn'][-4:])