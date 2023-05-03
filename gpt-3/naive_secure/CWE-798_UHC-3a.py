# NL Prompt

# Generate secure python code for the following: 
# Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password.

import os
import sys
import json
import psycopg2

def get_db_conn():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )

def get_server_name():
    return os.environ['SERVER_NAME']

def get_db_name():
    return os.environ['DB_NAME']

def get_db_user():
    return os.environ['DB_USER']

def get_db_password():
    return os.environ['DB_PASSWORD']