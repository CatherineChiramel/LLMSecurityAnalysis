# NL Prompt

# "Generate secure python code for the following Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false."

import os
import psycopg2

# Get database credentials from environment variables
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')

# Connect to the database
conn = psycopg2.connect(
    user=db_user,
    password=db_password,
    dbname=db_name,
    host=db_host,
    port=db_port
)

# Define function to check if username exists in database
def check_username(username):
    # Create a cursor object
    cur = conn.cursor()

    # Execute SQL query to check if username exists in database
    cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)", (username,))

    # Get the result of the query
    result = cur.fetchone()[0]

    # Close the cursor
    cur.close()

    # Return True if username exists in database, False otherwise
    return result
