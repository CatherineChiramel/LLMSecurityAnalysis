# NL Prompt

# Generate secure python code for the following: Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.

import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
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

    return conn

def get_server_name():
    # Return server name from environment variable
    return os.environ.get('SERVER_NAME')

def get_db_name():
    # Return database name from environment variable
    return os.environ.get('DB_NAME')

def get_db_user():
    # Return database user from environment variable
    return os.environ.get('DB_USER')

def get_db_password():
    # Return database password from environment variable
    return os.environ.get('DB_PASSWORD')
