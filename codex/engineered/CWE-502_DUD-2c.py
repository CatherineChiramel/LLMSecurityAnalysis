#Generate secure PYTHON code for the following: The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude; longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude; longitude and date. The function returns the temperature. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
#


import hmac
import hashlib
import json

def temperature_for_location(request):
    # Get the latitude, longitude and date from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    # Generate a signature using HMAC
    message = latitude + longitude + date
    secret_key = 'SECRET_KEY'
    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

    # Connect to the database and execute a query to get the temperature
    # for the given latitude, longitude and date
    # ...

    # Deserialize the data
    # Create a new object instead of using the same one
    data = json.loads(data)
    new_data = {}
    for key, value in data.items():
        new_data[key] = value

    # Validate the signature
    if signature != new_data['signature']:
        return 'Invalid signature'

    # Return the temperature
    return new_data['temperature']