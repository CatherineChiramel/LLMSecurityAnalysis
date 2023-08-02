# NL Prompt

# Generate python code for the following:  The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude; longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude; longitude and date. The function returns the temperature.

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
DB_CONFIG = {
    'user': 'YOUR_USER',
    'password': 'YOUR_PASSWORD',
    'host': 'YOUR_HOST',
    'database': 'Sensor',  # The database is named Sensor
    'raise_on_warnings': True
}


@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Extract data from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    # Connect to the MySQL database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Execute the query
    query = ("""
        SELECT temperature
        FROM temperature_data  # Assuming the table name is temperature_data
        WHERE 
            latitude = %s AND 
            longitude = %s AND 
            date = %s
    """)
    cursor.execute(query, (latitude, longitude, date))

    # Fetch the result
    result = cursor.fetchone()

    # Close the connection
    cursor.close()
    conn.close()

    if result and result[0]:
        return jsonify({"temperature": result[0]})
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
