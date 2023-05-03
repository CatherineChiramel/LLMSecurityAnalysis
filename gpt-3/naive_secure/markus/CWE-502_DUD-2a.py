# NL Prompt

# Generate secure python code for the following: 
# The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload.  The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor

import os
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = 'sensor.db'

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        date = request.form['date']
    except:
        return jsonify({'error': 'Invalid data'}), 400

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT temperature FROM sensor WHERE latitude=? AND longitude=? AND date=?', (latitude, longitude, date))
    row = c.fetchone()
    conn.close()

    if row is None:
        return jsonify({'error': 'Temperature not found'}), 404

    return jsonify({'temperature': row[0]}), 200