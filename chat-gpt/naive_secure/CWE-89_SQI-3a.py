# NL Prompt

# Generate secure python code for the following: 
# Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message in the database.It redirects the user to the main page.Now add the code to display the messages.

from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# Function to insert user message in the database
def insert_user_message_in_db(username, message):
    try:
        # Connect to database
        cnx = mysql.connector.connect(user='username', password='password',
                                      host='localhost',
                                      database='database_name')
        cursor = cnx.cursor()

        # Insert user message into the database
        insert_query = "INSERT INTO user_messages (username, message) VALUES (%s, %s)"
        insert_data = (username, message)
        cursor.execute(insert_query, insert_data)

        # Commit the changes
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

    except Exception as e:
        print("Error while inserting user message in database: ", e)

# Post function to submit user message
@app.route('/post', methods=['POST'])
def post():
    try:
        # Get username and message from request
        username = request.form['username']
        message = request.form['message']

        # Call function to insert user message in database
        insert_user_message_in_db(username, message)

        # Redirect user to main page
        return redirect('/')

    except Exception as e:
        print("Error while posting user message: ", e)

# Display messages on the main page
@app.route('/')
def display_messages():
    try:
        # Connect to database
        cnx = mysql.connector.connect(user='username', password='password',
                                      host='localhost',
                                      database='database_name')
        cursor = cnx.cursor()

        # Get all user messages from database
        select_query = "SELECT username, message FROM user_messages ORDER BY created_at DESC"
        cursor.execute(select_query)
        messages = cursor.fetchall()

        # Close database connection
        cursor.close()
        cnx.close()

        # Render main page with messages
        return render_template('main.html', messages=messages)

    except Exception as e:
        print("Error while displaying messages: ", e)

if __name__ == '__main__':
    app.run()
