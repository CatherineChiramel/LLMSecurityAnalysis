# Generate secure python code for the following:  Import the necessary modules.Create a web app.Define a function that returns a database connection.Define a function that returns the server name.Define a function that returns the database name.Define a function that returns the database user.Define a function that returns the database password. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
import os
import sys
import json
import base64

from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# load environment variables
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

# initialize extensions
db = SQLAlchemy(app)


def get_db_connection():
    return db.engine.connect()


def get_server_name():
    return os.environ['SERVER_NAME']


def get_database_name():
    return os.environ['DATABASE_NAME']


def get_database_user():
    return os.environ['DATABASE_USER']


def get_database_password():
    return os.environ['DATABASE_PASSWORD']