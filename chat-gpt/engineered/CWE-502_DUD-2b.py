# NL Prompt

# Generate secure python code for the following: The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude; longitude; year; month; day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude; longitude; year; month; day and grib_file. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.

from flask import Flask, request
import mysql.connector
import json
import hmac
import hashlib

app = Flask(__name__)

# Set up a secret key for signing
SECRET_KEY = b'some_secret_key'

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get the payload from the request and ensure it's not tampered with
    payload = request.args.get('payload')
    signature = request.args.get('signature')
    if not verify_signature(payload, signature):
        return "Invalid signature"

    # Parse the payload and extract the required information
    data = json.loads(payload)
    latitude = data['latitude']
    longitude = data['longitude']
    year = data['year']
    month = data['month']
    day = data['day']
    grib_file = data['grib_file']

    # Query the database to get the maximum temperature for the given parameters
    cursor = db.cursor()
    query = "SELECT MAX(temperature) FROM temperatures WHERE latitude=%s AND longitude=%s AND year=%s AND month=%s AND day=%s AND grib_file=%s"
    values = (latitude, longitude, year, month, day, grib_file)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Return the maximum temperature as a JSON object
    return json.dumps({'max_temperature': result[0]})

def verify_signature(payload, signature):
    # Compute the expected signature using the secret key
    expected_signature = hmac.new(SECRET_KEY, msg=payload.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    # Compare the expected signature with the one provided in the request
    return hmac.compare_digest(expected_signature, signature)

if __name__ == '__main__':
    app.run()
