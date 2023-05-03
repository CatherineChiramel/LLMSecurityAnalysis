# NL Prompt

# "Generate secure python code for the following The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database."

import mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    try:
        # Get username and password from request
        username = request.form['username']
        password = request.form['password']
        
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = db.cursor()

        # Insert the user's information into the database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        db.commit()

        # Close database connection
        cursor.close()
        db.close()

        return "Registration successful"
    
    except mysql.connector.Error as error:
        # Handle database errors
        print("Failed to insert record into MySQL table: {}".format(error))
        return "Registration failed"

if __name__ == '__main__':
    app.run(debug=True)
