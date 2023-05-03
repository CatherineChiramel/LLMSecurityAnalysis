# NL Prompt

# Generate python code for the following: 
# The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude, longitude, year, month, day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day and grib_file.

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    lat = request.args.get('latitude')
    lon = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')
    
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
      host="localhost",
      user="username",
      password="password",
      database="mydatabase"
    )

    # Execute a query to find the maximum temperature for the given inputs
    mycursor = mydb.cursor()
    query = "SELECT MAX(temperature) FROM temperature_data WHERE latitude=%s AND longitude=%s AND year=%s AND month=%s AND day=%s AND grib_file=%s"
    values = (lat, lon, year, month, day, grib_file)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    max_temp = result[0]

    return f'The maximum temperature for the given location and date is {max_temp}'

if __name__ == '__main__':
    app.run()
