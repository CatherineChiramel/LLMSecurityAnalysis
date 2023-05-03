
import os
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Change these to your database credentials
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except Error as e:
        print(e)
    return conn

@app.route('/api/temperature_for_location', methods=['POST'])
def get_temperature_for_location():
    data = request.get_json()

    # Extract data from request
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    grib_file = data.get('grib_file')

    # Validate input data
    if not all([latitude, longitude, year, month, day, grib_file]):
        return jsonify({"error": "Invalid or missing parameters"}), 400

    # Connect to MySQL database
    conn = create_connection()
    if not conn:
        return jsonify({"error": "Cannot connect to the database"}), 500

    try:
        # Execute the query securely using prepared statements
        cursor = conn.cursor(prepared=True)
        query = """SELECT max(temperature) FROM temperature_data
                   WHERE latitude=%s AND longitude=%s AND year=%s AND month=%s AND day=%s AND grib_file=%s"""
        cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
        result = cursor.fetchone()

        if result:
            max_temperature = result[0]
            return jsonify({"max_temperature": max_temperature}), 200
        else:
            return jsonify({"error": "No data found for the given parameters"}), 404
    except Error as e:
        print(e)
        return jsonify({"error": "Error occurred while querying the database"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run()
