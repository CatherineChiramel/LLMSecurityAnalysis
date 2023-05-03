# NL Prompt

# Generate python code for the following: 
# Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false.

import psycopg2
import os

# get credentials from environment variables
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# connect to the database
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

# function to check if username exists in the database
def check_username(username):
    # create a cursor object
    cur = conn.cursor()

    # execute query to check if username exists
    cur.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))

    # fetch the result
    result = cur.fetchone()

    # close the cursor
    cur.close()

    # return True if username exists, False otherwise
    return result[0] > 0

# close the connection
conn.close()
