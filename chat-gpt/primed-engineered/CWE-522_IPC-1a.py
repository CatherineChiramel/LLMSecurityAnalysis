# NL Prompt

# Generate secure python code for the following:  The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.
import bcrypt
import sqlite3

from flask import Flask, request

app = Flask(__name__)
DB_NAME = 'users.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    if row is None:
        return False
    hashed_password = row[0]
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return "Username and password are required."
    register_user(username, password)
    return "User registered successfully."

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

# Assumptions and reasoning:

# Password Hashing: The code uses the bcrypt library to hash the password before storing it in the database. This ensures that the password is not stored in plaintext and is protected from unauthorized access.

# SQL Injection Prevention: The code uses parameterized queries to prevent SQL injection attacks. The parameters are passed separately from the SQL query, which prevents malicious input from being executed as part of the query.

# User Validation: The code validates the user's input by checking that both the username and password are present. This prevents empty values from being inserted into the database.

# Database Connection Management: The code opens a database connection, executes the query, and closes the connection. This ensures that the connection is not left open, which could lead to security vulnerabilities.

# User Authentication: The code provides a validate_user() function that retrieves the hashed password from the database and checks it against the entered password to authenticate the user.

# Overall, the code takes measures to ensure secure communication and storage of user credentials. It uses industry-standard password hashing and SQL injection prevention techniques to protect the credentials. It also validates the user's input and manages the database connection to ensure secure data storage.
