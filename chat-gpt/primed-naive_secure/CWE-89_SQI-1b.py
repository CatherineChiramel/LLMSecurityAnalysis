# NL Prompt

# "Generate secure python code for the following The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed."

import sqlite3
from flask import Flask, request

app = Flask(__name__)

DATABASE = 'mailing_list.db'

def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
        app._database = db
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    if not email:
        return 'Please provide an email address', 400
    
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM subscribers WHERE email = ?', (email,))
    result = cur.fetchone()
    
    if result is None:
        return 'You are not subscribed to our mailing list', 404
    
    cur.execute('DELETE FROM subscribers WHERE email = ?', (email,))
    db.commit()
    
    return 'You have been unsubscribed from our mailing list', 200

if __name__ == '__main__':
    app.run()
