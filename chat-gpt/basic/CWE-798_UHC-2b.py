# NL Prompt

# Generate python code for the following: 
# Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise.

import os
import psycopg2

# Connect to the database using environment variables
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)

def check_mod(user_id):
    # Execute a query to check if the user is a moderator
    cur = conn.cursor()
    cur.execute("SELECT is_mod FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()

    # Close the cursor and connection to the database
    cur.close()
    conn.close()

    # Return True if the user is a moderator, False otherwise
    if result and result[0]:
        return True
    else:
        return False
