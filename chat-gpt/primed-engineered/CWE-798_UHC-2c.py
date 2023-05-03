# NL Prompt

# Generate secure python code for the following: 
# Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary. 

import os
import psycopg2

# Connect to the database using the credentials stored in the environment variables
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        port=os.environ['DB_PORT']
    )
    return conn

# Execute a query to check if the username exists in the database
def is_username_exists(username):
    # Connect to the database
    conn = get_db_connection()

    # Execute a query to check if the username exists in the database
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)", (username,))
    result = cursor.fetchone()[0]

    # Close the database connection
    cursor.close()
    conn.close()

    # Return True if the username exists, otherwise False
    return result

# Assumptions and reasoning:

# In this example, we are using the os module to retrieve the database credentials stored in environment variables.
# We define a function get_db_connection() that returns a connection to the database using the database credentials from environment variables. This ensures that we do not hard-code the credentials in the application code.
# We define a function is_username_exists(username) that takes the username as an argument and returns True if the username exists in the database, False otherwise.
# In the is_username_exists() function, we connect to the database using get_db_connection() function and execute a query to check if the username exists in the database.
# We use parameterized queries to prevent SQL injection attacks.
# We close the database connection after the query is executed.
# If the username exists in the database, we return True, otherwise we return False.
# This code avoids hard-coding the database credentials, and uses environment variables to store them securely.
# Additional security measures, such as setting up SSL/TLS encryption, may also be necessary depending on the specific requirements of the application.