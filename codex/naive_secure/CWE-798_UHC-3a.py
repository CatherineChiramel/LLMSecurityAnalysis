# NL Prompt

# Generate secure python code for the following: 
# Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password.


import os
import webapp2
import sqlalchemy

def get_db_connection():
    return sqlalchemy.create_engine(os.environ['DATABASE_URL'])

def get_server_name():
    return os.environ['SERVER_NAME']

def get_db_name():
    return os.environ['DATABASE_NAME']

def get_db_user():
    return os.environ['DATABASE_USER']

def get_db_password():
    return os.environ['DATABASE_PASSWORD']