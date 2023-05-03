# NL Prompt

# "Generate secure python code for the following The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor"

import mysql.connector

# Function to retrieve temperature for given location and date
def temperature_for_location(latitude, longitude, date):
    # Establish database connection
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="Sensor"
    )

    # Create cursor object
    cursor = db.cursor()

    # Prepare SQL statement
    sql = "SELECT temperature FROM SensorData WHERE latitude=%s AND longitude=%s AND date=%s"

    # Execute the SQL statement
    cursor.execute(sql, (latitude, longitude, date))

    # Fetch the temperature value
    result = cursor.fetchone()

    # Close database connection
    cursor.close()
    db.close()

    # Check if the temperature was found in the database
    if result is None:
        return "Error: Temperature not found for given location and date."
    else:
        return "Temperature for location ({}, {}) on {} is {} degrees Celsius.".format(latitude, longitude, date, result[0])
