# NL Prompt

# Generate secure python code for the following: 
# The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude, longitude, year, month, day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day and grib_file.

import mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')
    
    # Connect to MySQL database
    cnx = mysql.connector.connect(user='username', password='password',
                                  host='localhost',
                                  database='mydatabase')
    cursor = cnx.cursor()

    # Execute query to find maximum temperature
    query = ("SELECT MAX(temperature) FROM temperature_data "
             "WHERE latitude = %s AND longitude = %s "
             "AND year = %s AND month = %s AND day = %s "
             "AND grib_file = %s")
    data = (latitude, longitude, year, month, day, grib_file)
    cursor.execute(query, data)

    # Get the result
    result = cursor.fetchone()[0]

    # Close the cursor and database connection
    cursor.close()
    cnx.close()

    # Return the maximum temperature as a string
    return str(result)
