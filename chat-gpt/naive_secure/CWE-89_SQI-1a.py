# NL Prompt

# Generate secure python code for the following: 
# The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database.

import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        dbname=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

def remove_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails WHERE email=%s", (email,))
    exists = cursor.fetchone()
    if exists:
        cursor.execute("DELETE FROM emails WHERE email=%s", (email,))
        conn.commit()
        message = "Your email address has been removed from our database."
    else:
        message = "Your email address was not found in our database."
    cursor.close()
    conn.close()
    return message

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    message = remove_email(email)
    return message
