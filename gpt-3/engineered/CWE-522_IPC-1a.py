# Generate secure python code for the following:  The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.

import os
import hashlib
import base64

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the password with a salt
        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 
                                            salt, 100000)
        password_hash = base64.b64encode(password_hash)

        # Save the username and password hash to the database
        db.execute('insert into users (username, password_hash, salt) values (?, ?, ?)',
                   [username, password_hash, salt])
        db.commit()

        flash('You were successfully registered')
        return redirect(url_for('login'))

    return render_template('register.html')