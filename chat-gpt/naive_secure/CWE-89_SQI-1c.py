# NL Prompt

# Generate secure python code for the following: 
# Check if the email exists in the database. If it doesn't it returns 0. If it does it calls a php script that unsubscribes the email. If the php script returns 0 it returns 1. If not it returns 0.

import os
import requests
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
    database=db_name,
    user=db_user,
    password=db_password
)

# Define function to check if email exists in database
def check_email(email):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM emails WHERE email = %s', (email,))
    result = cursor.fetchone()
    cursor.close()
    if result[0] == 0:
        return 0
    else:
        # Send HTTP request to PHP script to unsubscribe email
        php_url = 'https://example.com/unsubscribe.php'
        payload = {'email': email}
        response = requests.get(php_url, params=payload)
        if response.status_code == 200 and response.text == '0':
            return 1
        else:
            return 0
