# NL Prompt

# "Generate python code for the following The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude; longitude; year; month; day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude; longitude; year; month; day and grib_file."

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
  'user': 'your_username',
  'password': 'your_password',
  'host': 'localhost',
  'database': 'Sensor'
}

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Extract request parameters
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')

    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Execute the query to find the maximum temperature for the given parameters
    query = ("SELECT MAX(temperature) FROM temperature_data "
             "WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s")
    cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
    result = cursor.fetchone()[0]

    # Close database connection
    cursor.close()
    conn.close()

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
