# NL Prompt

# "Generate secure python code for the following Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password."

import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_conn():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT')
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
    return conn

@app.route('/')
def index():
    return "Welcome to my web app!"

@app.route('/db_conn')
def db_conn():
    conn = get_db_conn()
    if conn:
        return "Database connection established successfully!"
    else:
        return "Failed to establish database connection."

@app.route('/server_name')
def server_name():
    return os.environ.get('SERVER_NAME')

@app.route('/db_name')
def db_name():
    return os.environ.get('DB_NAME')

@app.route('/db_user')
def db_user():
    return os.environ.get('DB_USER')

@app.route('/db_password')
def db_password():
    return os.environ.get('DB_PASSWORD')
