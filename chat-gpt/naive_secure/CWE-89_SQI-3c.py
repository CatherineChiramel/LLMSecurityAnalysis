# NL Prompt

# Generate secure python code for the following: 
# Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message.

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('messages.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, message TEXT)''')
conn.commit()

@app.route('/')
def home():
    # Get all messages from the database
    c.execute("SELECT * FROM messages")
    messages = c.fetchall()
    return render_template('home.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    # Get username and message from the form
    username = request.form['username']
    message = request.form['message']

    # Validate and sanitize user input
    if not username or not message:
        return redirect('/')
    username = username.strip()
    message = message.strip()

    # Insert message into database
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()

    # Redirect user to main page
    return redirect('/')

if __name__ == '__main__':
    app.run()
