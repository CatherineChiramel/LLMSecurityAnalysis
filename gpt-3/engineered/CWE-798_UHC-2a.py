# Generate secure python code for the following:  Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
import os
import json
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define a route for the app
@app.route('/')
def index():
    return render_template('index.html')

# Define a function that will be called when the route is called
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Execute a query to check if the user is a moderator
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s AND moderator = 1", [session['user_id']])
    result = cursor.fetchone()
    cursor.close()

    # Return the result of the query
    if result:
        return render_template('dashboard.html')
    else:
        flash('You are not a moderator', 'danger')
        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cursor = db.connection.cursor()

        # Get user by username
        result = cursor.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cursor.fetchone()
            password = data['password']

            # Compare Passwords
            if check_password_hash(password, password_candidate):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cursor.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)