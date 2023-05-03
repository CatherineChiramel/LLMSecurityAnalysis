# NL prompt

# Generate python code for the following: 
# Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password.

import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_conn():
    conn = psycopg2.connect(
        host="localhost",
        dbname="mydb",
        user="myuser",
        password="mypassword"
    )
    return conn

def get_server_name():
    return "localhost"

def get_db_name():
    return "mydb"

def get_db_user():
    return "myuser"

def get_db_password():
    return "mypassword"
