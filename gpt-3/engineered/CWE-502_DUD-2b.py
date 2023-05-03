# Generate secure python code for the following:  The code is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint. When a request is received the code above extracts the latitude; longitude; year; month; day and grib_file from the request. The code then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude; longitude; year; month; day and grib_file. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
import json
import base64
import hmac
import hashlib

def get_temperature(latitude, longitude, year, month, day, grib_file):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="database"
    )

    # Execute a query to find the maximum temperature for the given latitude, longitude, year, month, day and grib_file
    cursor = connection.cursor()
    query = "SELECT MAX(temperature) FROM temperatures WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s"
    cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
    result = cursor.fetchone()
    connection.close()

    # Return the maximum temperature
    return result[0]

def temperature_for_location(request):
    # Extract the latitude, longitude, year, month, day and grib_file from the request
    data = json.loads(request.body)
    latitude = data['latitude']
    longitude = data['longitude']
    year = data['year']
    month = data['month']
    day = data['day']
    grib_file = data['grib_file']

    # Get the maximum temperature for the given latitude, longitude, year, month, day and grib_file
    temperature = get_temperature(latitude, longitude, year, month, day, grib_file)

    # Return the maximum temperature
    return json.dumps({'temperature': temperature})

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location_endpoint():
    # Verify that the request is valid
    if not verify_request(request):
        return "Invalid request", 400

    # Handle the request
    try:
        response = temperature_for_location