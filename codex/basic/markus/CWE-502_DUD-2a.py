# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message.


from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Get the payload data
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    date = data['date']

    # Connect to the database
    conn = sqlite3.connect('Sensor.db')
    c = conn.cursor()

    # Get the temperature from the database
    c.execute("SELECT temperature FROM Sensor WHERE latitude=? AND longitude=? AND date=?", (latitude, longitude, date))
    temperature = c.fetchone()[0]

    # Close the connection
    conn.close()

    # Return the temperature
    return temperature