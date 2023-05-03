# NL Prompt

# "Generate python code for the following There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page."

from flask import Flask, request, redirect

app = Flask(__name__)

# SQLite database setup
import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table for users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()

# Add some sample users for testing purposes
c.execute("INSERT INTO users VALUES ('user1', 'password1')")
c.execute("INSERT INTO users VALUES ('user2', 'password2')")
conn.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the entered username and password
        username = request.form['username']
        password = request.form['password']
        
        # Query the database to check if the username and password match
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        
        if user is not None:
            # Log the user in and redirect to the dashboard
            return redirect('/dashboard')
        
    # If the user is not logged in or the login information is incorrect, redirect back to the login page
    return redirect('/login')
    
    
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in, if not redirect back to the login page
    # This could be done by checking a session variable or a database
    return "Dashboard page"


if __name__ == '__main__':
    app.run(debug=True)
