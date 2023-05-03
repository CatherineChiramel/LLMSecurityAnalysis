# NL Prompt

# Generate secure python code for the following: 
# The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude, longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date. The function returns the temperature.

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get latitude, longitude, and date from request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    # Connect to database
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="yourdatabase"
    )

    # Execute query to get temperature for given latitude, longitude, and date
    mycursor = mydb.cursor()
    query = "SELECT temperature FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s"
    values = (latitude, longitude, date)
    mycursor.execute(query, values)
    temperature = mycursor.fetchone()

    # Close database connection
    mydb.close()

    # Return temperature
    return jsonify({'temperature': temperature[0]})
