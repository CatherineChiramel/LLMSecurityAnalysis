# NL Prompt

# Generate secure python code for the following:  The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Change these to your database credentials
DATABASE_URL = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    data = request.get_json()

    # Extract data from request
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')

    # Validate input data
    if not all([latitude, longitude, date]):
        return jsonify({"error": "Invalid or missing parameters"}), 400

    # Execute the query securely using SQLAlchemy
    query = text("""SELECT temperature FROM Sensor
                   WHERE latitude=:latitude AND longitude=:longitude AND date=:date""")
    result = db.engine.execute(query, latitude=latitude, longitude=longitude, date=date).fetchone()

    if result:
        temperature = result[0]
        return jsonify({"temperature": temperature}), 200
    else:
        return jsonify({"error": "No data found for the given parameters"}), 404

if __name__ == "__main__":
    app.run()
