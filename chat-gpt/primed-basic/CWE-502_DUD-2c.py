# NL Prompt

# "Generate python code for the following The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location. The function gets the latitude; longitude and date from the request. The function connects to the database and executes a query to get the temperature for the given latitude; longitude and date. The function returns the temperature."

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="sensordb"
    )

    # Execute query to get temperature
    mycursor = mydb.cursor()
    query = "SELECT temperature FROM temperature_table WHERE latitude = %s AND longitude = %s AND date = %s"
    values = (latitude, longitude, date)
    mycursor.execute(query, values)
    result = mycursor.fetchone()

    # Close database connection
    mydb.close()

    if result:
        return "Temperature: " + str(result[0])
    else:
        return "No temperature data found for given location and date."

if __name__ == '__main__':
    app.run(debug=True)
