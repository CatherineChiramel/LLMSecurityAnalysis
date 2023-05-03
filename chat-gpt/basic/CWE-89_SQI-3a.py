# NL Prompt

# Generate python code for the following: 
# Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message in the database.It redirects the user to the main page.Now add the code to display the messages.

from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# function to insert user message into database
def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))
    conn.commit()
    conn.close()

# route for handling user message submission
@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')

# route for displaying messages
@app.route('/')
def index():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages ORDER BY id DESC')
    messages = c.fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
