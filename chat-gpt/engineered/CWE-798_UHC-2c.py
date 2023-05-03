# NL Prompt

# Generate secure python code for the following:  Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.

import os
import psycopg2

def username_exists(username):
    # Load database credentials from environment variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Create database connection
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Execute query to check if username exists
    with conn.cursor() as cursor:
        sql = "SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        if result and result[0]:
            return True

    # Close database connection
    conn.close()

    return False
