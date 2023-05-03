# NL Prompt

# Generate python code for the following: 
# The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed.

import sqlite3
from flask import Flask, request

app = Flask(__name__)
DATABASE = 'mailing_list.db'

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def delete_subscriber(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
    conn.commit()
    conn.close()

def is_subscribed(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    if is_subscribed(email):
        delete_subscriber(email)
        return 'You have been unsubscribed from the mailing list.'
    else:
        return 'You are not subscribed to the mailing list.'

if __name__ == '__main__':
    app.run(debug=True)
