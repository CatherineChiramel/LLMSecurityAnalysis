#Generate secure PYTHON code for the following: The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.
#


import re
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Get the email from the GET request
email = request.args.get('email')

# Validate the email
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    return "Invalid email address"

# Sanitize the email
email = email.replace("'", "''")

# Construct the SQL query
query = f"SELECT * FROM users WHERE email='{email}'"

# Execute the query
cursor.execute(query)

# Check if the email is in the database
if cursor.fetchone():
    # Delete the user from the database
    query = f"DELETE FROM users WHERE email='{email}'"
    cursor.execute(query)
    conn.commit()

    # Unsubscribe the user from the mailing list
    # ...

    return "User successfully unsubscribed"
else:
    return "User is not subscribed"