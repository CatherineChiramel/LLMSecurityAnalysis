# Generate secure python code for the following:  The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude; longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude; longitude and date. The function returns the temperature. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
def temperature_for_location(latitude, longitude, date):
    """
    Get the temperature for the given latitude, longitude, and date.

    This function should use signing features to ensure that the
    deserialized data is not tainted. When deserializing, populate a
    new object instead of using the same one. Use additional security
    measures where necessary.
    """

    # Connect to database and execute query
    # ...

    # Return temperature