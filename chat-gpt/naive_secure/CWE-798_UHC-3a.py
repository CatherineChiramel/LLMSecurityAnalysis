# NL Prompt

# Generate secure python code for the following: 
# Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password.

import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_SERVER'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

def get_db_server_name():
    return os.environ.get('DB_SERVER')

def get_db_name():
    return os.environ.get('DB_NAME')

def get_db_user():
    return os.environ.get('DB_USER')

def get_db_password():
    return os.environ.get('DB_PASSWORD')
