# NL Prompt

# Generate python code for the following: 
# The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude, longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date. The function returns the temperature.

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get the latitude, longitude and date from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')
    
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    
    # Execute a query to get the temperature for the given latitude, longitude and date
    cursor = db.cursor()
    query = "SELECT temperature FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s"
    values = (latitude, longitude, date)
    cursor.execute(query, values)
    
    # Get the result of the query
    result = cursor.fetchone()
    
    # Close the database connection
    db.close()
    
    # Return the temperature
    if result:
        return str(result[0])
    else:
        return "Temperature not found"
