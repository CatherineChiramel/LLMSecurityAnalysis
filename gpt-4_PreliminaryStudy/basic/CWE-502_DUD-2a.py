# NL Prompt

# Generate python code for the following:  The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite database named "sensor.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)


@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Get payload data
    payload = request.json
    latitude = payload.get('latitude')
    longitude = payload.get('longitude')
    date = payload.get('date')

    # Fetch the temperature from the database
    record = Temperature.query.filter_by(
        latitude=latitude, longitude=longitude, date=date).first()

    if record:
        return jsonify({"temperature": record.temperature})
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist yet
    app.run(debug=True)
