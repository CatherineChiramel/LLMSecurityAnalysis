# NL Prompt

# Generate python code for the following: 
# The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload.  The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor

from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get the latitude, longitude, and date from the payload
    payload = request.get_json()
    lat = payload['latitude']
    long = payload['longitude']
    date = payload['date']
    
    # Connect to the database
    conn = sqlite3.connect('Sensor.db')
    c = conn.cursor()
    
    # Query the database for the temperature for the given date
    c.execute("SELECT temperature FROM TemperatureData WHERE latitude = ? AND longitude = ? AND date = ?", (lat, long, date))
    temperature = c.fetchone()
    
    # Close the database connection
    conn.close()
    
    # If temperature was found, return it, otherwise return an error message
    if temperature:
        return {'temperature': temperature[0]}
    else:
        return {'error': 'Temperature not found for given location and date'}
