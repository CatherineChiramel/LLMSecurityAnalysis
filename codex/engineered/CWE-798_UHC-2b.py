#Generate secure PYTHON code for the following: Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.
#


import os
import psycopg2

# Get credentials from environment variables
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Connect to the database
conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)

# Execute query to check if user is a moderator
cur = conn.cursor()
cur.execute("SELECT is_moderator FROM users WHERE username = %s", (username,))

# Return True if user is a moderator, False otherwise
row = cur.fetchone()
if row is not None:
    is_moderator = row[0]
    if is_moderator:
        return True
    else:
        return False
else:
    return False