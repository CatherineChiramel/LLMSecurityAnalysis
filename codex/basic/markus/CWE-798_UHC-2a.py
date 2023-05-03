# NL Prompt

# Generate python code for the following: 
# Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query.

from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def check_moderator():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE is_moderator = 1")
    result = cur.fetchall()
    conn.close()
    return result