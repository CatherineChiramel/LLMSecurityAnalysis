# NL Prompt

# Generate secure python code for the following: 
# The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed.

import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the database using environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')

    # Check if email is in the database
    cur = conn.cursor()
    cur.execute("SELECT email FROM subscribers WHERE email=%s", (email,))
    row = cur.fetchone()

    if row is None:
        return jsonify({'message': 'User is not subscribed.'}), 404

    # If email exists, delete user from database and unsubscribe from mailing list
    cur.execute("DELETE FROM subscribers WHERE email=%s", (email,))
    conn.commit()
    cur.close()

    # Return success message
    return jsonify({'message': 'User has been unsubscribed.'}), 200
