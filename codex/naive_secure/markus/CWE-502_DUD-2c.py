# NL Prompt

# Generate secure python code for the following: 
# The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude, longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date. The function returns the temperature.
 
@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    date = request.args.get('date')
    temperature = get_temperature(latitude,longitude,date)
    return str(temperature)
