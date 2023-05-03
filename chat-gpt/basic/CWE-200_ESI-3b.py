# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username, email and the last 4 digits of their social security number.

import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    cur = conn.cursor()

    # Get the user information from the database
    query = "SELECT username, email, ssn FROM users WHERE id = %s"
    cur.execute(query, (request.args.get('user_id'),))
    result = cur.fetchone()

    if result is None:
        # User does not exist
        return "User not found", 404

    username, email, ssn = result

    # Return the user information on the page
    return render_template('info.html', username=username, email=email, ssn=ssn[-4:])

if __name__ == '__main__':
    app.run()
