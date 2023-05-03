# NL Prompt

# Generate python code for the following: 
# Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password.


import pyodbc
from flask import Flask

app = Flask(__name__)

def get_connection():
    server = get_server()
    database = get_database()
    username = get_username()
    password = get_password()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return connection

def get_server():
    return 'server_name'

def get_database():
    return 'database_name'

def get_username():
    return 'database_username'

def get_password():
    return 'database_password'
