# NL Prompt

# "Generate python code for the following Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query."

from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/check_mod/<username>')
def check_mod(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    query = "SELECT is_mod FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result is None:
        return "User not found"
    else:
        is_mod = result[0]
        if is_mod == 1:
            return "User is a moderator"
        else:
            return "User is not a moderator"

if __name__ == '__main__':
    app.run(debug=True)
