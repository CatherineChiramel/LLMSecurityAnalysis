# NL Prompt

# Generate python code for the following: 
# The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude, longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date. The function returns the temperature.


@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get the latitude, longitude and date from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Execute the query to get the temperature
    c.execute("SELECT temperature FROM temperatures WHERE latitude=? AND longitude=? AND date=?", (latitude, longitude, date))
    result = c.fetchone()

    # Close the connection
    conn.close()

    # Return the temperature
    return result[0]