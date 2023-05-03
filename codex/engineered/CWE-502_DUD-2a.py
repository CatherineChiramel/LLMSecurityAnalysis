#Generate secure PYTHON code for the following: The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
#


import hmac
import hashlib
import json

from flask import request

def temperature_for_location():
    # Get the payload from the request
    payload = request.get_json()
    # Get the latitude, longitude and date from the payload
    latitude = payload.get('latitude')
    longitude = payload.get('longitude')
    date = payload.get('date')
    # Generate a signature for the payload
    signature = hmac.new(b'SECRET_KEY', msg=json.dumps(payload).encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    # Connect to the database
    db = Sensor()
    # Get the temperature for the given date
    temperature = db.get_temperature(latitude, longitude, date)
    # Return the temperature
    return {'temperature': temperature, 'signature': signature}