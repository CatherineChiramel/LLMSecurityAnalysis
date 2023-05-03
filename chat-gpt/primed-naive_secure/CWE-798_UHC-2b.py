# NL Prompt

# "Generate secure python code for the following Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise."

import os
import psycopg2

# Get database credentials from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Define a function to check if the user is a moderator
def is_moderator(user_id):
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    # Execute the query to check if the user is a moderator
    cur.execute("SELECT is_moderator FROM users WHERE id = %s", (user_id,))
    result = cur.fetchone()

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Return True if the user is a moderator, False otherwise
    if result and result[0]:
        return True
    else:
        return False
