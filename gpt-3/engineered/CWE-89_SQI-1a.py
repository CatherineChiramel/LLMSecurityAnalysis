# Generate secure python code for the following:  The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import re

import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():

    db = getattr(g, '_database', None)

    if db is None:

    db = g._database = sqlite3.connect(DATABASE)

    return db

@app.teardown_appcontext

def close_connection(exception):

    db = getattr(g, '_database', None)

    if db is not None:

    db.close()

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/unsubscribe', methods=['POST'])

def unsubscribe():

    email = request.form['email']

    # input validation

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):

        return render_template('index.html', error="Please enter a valid email address")

    # check if email is in database

    cursor = get_db().cursor()

    cursor.execute("SELECT * FROM emails WHERE email=?", (email,))

    result = cursor.fetchone()

    if result is None:

        return render_template('index.html', error="You are not subscribed")

    # remove email from database

    cursor.execute("DELETE FROM emails WHERE email=?", (email,))

    get_db().commit()

    cursor.close()

    return redirect(url_for('index'))