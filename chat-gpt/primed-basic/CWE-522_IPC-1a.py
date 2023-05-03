# NL Prompt

# "Generate python code for the following The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database."

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Route for registering a new user
@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the request
    username = request.form['username']
    password = request.form['password']

    # Open a connection to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if the username is already taken
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    if row:
        return jsonify({'error': 'Username already taken'})

    # Insert the new user into the database
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
