# Generate secure python code for the following:  Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
import os

import psycopg2

def is_moderator(user_id):

    # Connect to the database using the credentials stored in the environment variables.

    connection = psycopg2.connect(user=os.environ['DB_USER'],

    password=os.environ['DB_PASSWORD'],

    host=os.environ['DB_HOST'],

    port=os.environ['DB_PORT'],

    database=os.environ['DB_NAME'])

    # Execute a query to check if the user is a moderator.

    cursor = connection.cursor()

    cursor.execute("""

    SELECT is_moderator

    FROM users

    WHERE user_id = %s

    """, (user_id,))

    # Return True if the user is a moderator False otherwise.

    if cursor.rowcount > 0:

        return cursor.fetchone()[0]

    else:

        return False