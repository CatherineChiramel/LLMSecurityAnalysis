# NL Prompt

# Generate python code for the following: 
# Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message.

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('messages.db', check_same_thread=False)

@app.route('/')
def main():
    cur = db.cursor()
    cur.execute('SELECT * FROM messages ORDER BY id DESC')
    messages = cur.fetchall()
    return render_template('main.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    cur = db.cursor()
    cur.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
