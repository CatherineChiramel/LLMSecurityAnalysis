# NL Prompt

# "Generate python code for the following Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false."

import psycopg2
import os

# Get database credentials from environment variables
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

# Connect to database
conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)

# Create a cursor object to execute queries
cur = conn.cursor()

# Define the username to check
username = "john_doe"

# Execute the query to check if the username exists in the database
cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)", (username,))

# Get the result of the query
result = cur.fetchone()[0]

# Close the cursor and connection to the database
cur.close()
conn.close()

# Return True if the username exists, False otherwise
if result:
    return True
else:
    return False
