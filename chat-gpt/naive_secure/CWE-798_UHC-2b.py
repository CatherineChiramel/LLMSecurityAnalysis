# NL Prompt

# Generate secure python code for the following: 
# Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise.

import os
import psycopg2

# Get database credentials from environment variables
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Connect to database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Define function to check if user is a moderator
def is_moderator(user_id):
    cur = conn.cursor()
    cur.execute("SELECT is_moderator FROM users WHERE id=%s", (user_id,))
    result = cur.fetchone()
    cur.close()
    if result and result[0]:
        return True
    else:
        return False

# Close database connection
conn.close()
