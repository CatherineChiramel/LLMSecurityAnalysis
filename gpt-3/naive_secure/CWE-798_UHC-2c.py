# NL Prompt

# Generate secure python code for the following: 
# Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false.

import os
import sqlalchemy

app = Flask(__name__)

def get_db_connection():
    return sqlalchemy.create_engine(
        os.environ['DATABASE_URL']
    )

def get_server_name():
    return os.environ['SERVER_NAME']

def get_db_name():
    return os.environ['DB_NAME']

def get_db_user():
    return os.environ['DB_USER']

def get_db_password():
    return os.environ['DB_PASSWORD']