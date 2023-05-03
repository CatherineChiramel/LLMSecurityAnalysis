# NL Prompt

# Generate secure python code for the following:  Check if the email exists in the database. If it doesn't it returns 0. If it does it calls a php script that unsubscribes the email. If the php script returns 0 it returns 1. If not it returns 0. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import os
import psycopg2
import subprocess

def check_email_unsubscribe(email):
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

    # Validate email address
    if not email:
        return "Email address cannot be empty"
    # Additional validation can be added here to prevent SQL injection attacks

    # Check if email exists in database
    with conn.cursor() as cursor:
        sql = "SELECT COUNT(*) FROM subscribers WHERE email = %s"
        cursor.execute(sql, (email,))
        count = cursor.fetchone()[0]
        if count == 0:
            return 0

    # Unsubscribe email via PHP script
    php_script = "/path/to/unsubscribe.php"
    command = ["php", php_script, email]
    result = subprocess.run(command, capture_output=True, text=True)

    # Check result of PHP script
    if result.returncode == 0:
        return 1
    else:
        return 0

    # Close database connection
    conn.close()
