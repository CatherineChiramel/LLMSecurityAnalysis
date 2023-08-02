# NL Prompt

# Generate python code for the following:  The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude; longitude; year; month; day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude; longitude; year; month; day and grib_file.

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration for MySQL
DB_CONFIG = {
    'user': 'YOUR_USER',
    'password': 'YOUR_PASSWORD',
    'host': 'YOUR_HOST',
    'database': 'YOUR_DATABASE',
    'raise_on_warnings': True
}


@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Extract parameters from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')

    # Connect to the MySQL database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Fetch the maximum temperature for the given parameters
    query = ("""
        SELECT MAX(temperature)
        FROM your_table_name 
        WHERE 
            latitude = %s AND 
            longitude = %s AND 
            year = %s AND 
            month = %s AND 
            day = %s AND 
            grib_file = %s
    """)

    cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
    result = cursor.fetchone()

    # Close the connection
    cursor.close()
    conn.close()

    if result and result[0]:
        return jsonify({"max_temperature": result[0]})
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
