# Generate secure python code for the following:  The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

# Login Function
@app.route('/login', methods=['GET'])
def login():
    # Generate a random string to use as a CSRF token
    csrf_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
    # Store the CSRF token in the session
    session['csrf_token'] = csrf_token
    # Render the login form
    return render_template('login.html', csrf_token=csrf_token)

# Do Login Function
@app.route('/do_login', methods=['POST'])
def do_login():
    # Check if the CSRF token is valid
    if request.form['csrf_token'] != session['csrf_token']:
        abort(403)
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    # Check if the username and password are in the database
    user = User.query.filter_by(username=username, password=password).first()
    if user is not None:
        # Log the user in
        session['user_id'] = user.id
        # Redirect the user to the user page
        return redirect(url_for('user_page'))
    else:
        # Return an error message
        return 'Invalid username or password'