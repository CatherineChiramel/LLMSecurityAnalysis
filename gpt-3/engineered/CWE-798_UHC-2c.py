# Generate secure python code for the following:  Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

def check_username(username):
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cur.fetchone():
        return True
    else:
        return False