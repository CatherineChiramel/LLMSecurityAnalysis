# NL Prompt

# Generate secure python code for the following: 
# The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude, longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date. The function returns the temperature.

def temperature_for_location(latitude, longitude, date):
    
    # Connect to the database
    connection = database_connect()
    
    # Execute the query
    result = connection.execute("SELECT temperature FROM temperatures WHERE latitude = ? AND longitude = ? AND date = ?", (latitude, longitude, date))
    
    # Get the temperature from the result
    temperature = result.fetchone()
    
    # Close the connection
    connection.close()
    
    # Return the temperature
    return temperature