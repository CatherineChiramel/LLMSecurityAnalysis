# NL Prompt

# Generate secure python code for the following: 
# The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload.  The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor

import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        # Get the latitude, longitude, and date from the request payload
        data = request.json
        latitude = data['latitude']
        longitude = data['longitude']
        date = data['date']

        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="Sensor"
        )

        # Query the database for the temperature for the given date and location
        mycursor = mydb.cursor()
        sql = "SELECT temperature FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s"
        val = (latitude, longitude, date)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        # Return the temperature
        if result is not None:
            temperature = result[0]
            return jsonify({'temperature': temperature})
        else:
            return jsonify({'error': 'Temperature data not found for given location and date'})

    except Exception as e:
        return jsonify({'error': str(e)})
