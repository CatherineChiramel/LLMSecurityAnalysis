# NL Prompt

# Generate python code for the following: 
# Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query.

from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/check-moderator/<username>')
def check_moderator(username):
    # Connect to the database
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )

    # Execute a query to check if the user is a moderator
    cur = conn.cursor()
    cur.execute("SELECT is_moderator FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    # Close the database connection
    cur.close()
    conn.close()

    # Return the result of the query
    if result is not None:
        return f"{username} is a moderator: {result[0]}"
    else:
        return f"{username} not found in database"

if __name__ == '__main__':
    app.run(debug=True)
