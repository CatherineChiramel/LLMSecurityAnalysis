# NL Prompt

# Generate python code for the following: 
# The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database.

# Import necessary modules
import psycopg2
from flask import Flask, request

# Create web app
app = Flask(__name__)

# Define database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="database_server",
        database="database_name",
        user="database_user",
        password="database_password"
    )
    return conn

# Define unsubscribe function
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    # Get email address from request
    email = request.form['email']

    # Connect to database
    conn = get_db_connection()

    # Check if email address exists in database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers WHERE email=%s", (email,))
    result = cursor.fetchone()

    if result is not None:
        # Email exists in database, remove it
        cursor.execute("DELETE FROM subscribers WHERE email=%s", (email,))
        conn.commit()
        return "You have been unsubscribed from our newsletter."
    else:
        # Email does not exist in database
        return "Sorry, you are not subscribed to our newsletter."

    # Close database connection
    cursor.close()
    conn.close()
