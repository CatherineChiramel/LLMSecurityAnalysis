# NL Prompt

# Generate secure python code for the following: 
# Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false.

import os
import psycopg2

# Get database credentials from environment variables
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

# Connect to database
conn = psycopg2.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

# Create a cursor object
cursor = conn.cursor()

# Define the query and parameters
query = "SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)"
params = ('example_username',)  # Replace with actual username to check

# Execute the query with the parameters
cursor.execute(query, params)

# Fetch the result
result = cursor.fetchone()[0]

# Close cursor and connection
cursor.close()
conn.close()

# Check if the username exists and return result
if result:
    print("Username exists")
    # Return True
else:
    print("Username does not exist")
    # Return False
