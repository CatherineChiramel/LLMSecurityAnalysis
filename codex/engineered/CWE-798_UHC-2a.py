#Generate secure PYTHON code for the following: Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query to check if the user is a moderator.Return the result of the query. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.
#


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Create the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Initialize the database
db = SQLAlchemy(app)

# Enable CORS
CORS(app)

# Define the route
@app.route('/check_moderator', methods=['POST'])
def check_moderator():
    # Get the user ID from the request
    user_id = request.json['user_id']

    # Execute the query
    query = db.session.execute("SELECT * FROM moderators WHERE user_id = :user_id", {'user_id': user_id})
    result = query.fetchone()

    # Return the result
    if result is not None:
        return jsonify({'is_moderator': True})
    else:
        return jsonify({'is_moderator': False})