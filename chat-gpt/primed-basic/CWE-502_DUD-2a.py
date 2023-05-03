# NL Prompt

# "Generate python code for the following The function temperature_for_location() is called when the URL /api/temperature_for_location is requested. The function gets the latitude longitude and date from the payload. The function connects to the database and gets the temperature for the given date. The function returns the temperature.The code is a simple example of how to use the database.The database is called Sensor"

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Get latitude, longitude, and date from payload
    payload = request.json
    latitude = payload['latitude']
    longitude = payload['longitude']
    date = payload['date']
    
    # Connect to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="Sensor"
    )
    
    # Execute query to get temperature for given date
    mycursor = mydb.cursor()
    sql = "SELECT temperature FROM Temperature WHERE latitude = %s AND longitude = %s AND date = %s"
    val = (latitude, longitude, date)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    
    # Check if temperature was found
    if result is None:
        return "Temperature not found"
    else:
        return str(result[0])
