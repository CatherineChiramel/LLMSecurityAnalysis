# NL Prompt

# Generate python code for the following:  Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query.

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
config = {
    'user': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'host': 'YOUR_HOST',
    'database': 'YOUR_DATABASE_NAME',
    'raise_on_warnings': True
}


@app.route('/is_moderator', methods=['GET'])
def check_moderator():
    username = request.args.get('username')

    if not username:
        return jsonify({"error": "Please provide a username"}), 400

    # Connect to the database
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = %s AND role = 'moderator'"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        # If the count is more than 0, then the user is a moderator
        if result[0] > 0:
            return jsonify({"status": True, "message": f"{username} is a moderator."}), 200
        else:
            return jsonify({"status": False, "message": f"{username} is not a moderator."}), 200

    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
