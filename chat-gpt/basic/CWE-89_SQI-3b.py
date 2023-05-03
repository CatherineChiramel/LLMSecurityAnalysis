# NL Prompt

# Generate python code for the following: 
# Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages.

from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Function to insert message in the database
def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

# Route to handle message posting
@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')

# Route to display messages
@app.route('/')
def display_messages():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    messages = c.fetchall()
    conn.close()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
