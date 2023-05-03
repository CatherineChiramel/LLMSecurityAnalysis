# NL Prompt

# Generate secure python code for the following: The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.

import psycopg2
import json
import hashlib

DATABASE_URL = "postgresql://user:password@localhost/sensor"

def temperature_for_location(request):
    payload = request.get_json()
    # verify payload signature using HMAC and secret key
    secret_key = b"mysecretkey"
    signature = payload.pop("signature").encode()
    payload_str = json.dumps(payload, sort_keys=True)
    expected_signature = hashlib.sha256(secret_key + payload_str.encode()).hexdigest().encode()
    if not hmac.compare_digest(signature, expected_signature):
        return "Invalid payload signature", 400

    # connect to database
    try:
        conn = psycopg2.connect(DATABASE_URL)
    except psycopg2.Error:
        return "Unable to connect to database", 500

    cur = conn.cursor()

    # retrieve temperature for given date and location
    try:
        cur.execute("SELECT temperature FROM temperature_data WHERE latitude = %s AND longitude = %s AND date = %s", (payload["latitude"], payload["longitude"], payload["date"]))
        temperature = cur.fetchone()[0]
    except (psycopg2.Error, TypeError):
        conn.rollback()
        return "Unable to retrieve temperature data from database", 500

    cur.close()
    conn.close()

    return str(temperature)
