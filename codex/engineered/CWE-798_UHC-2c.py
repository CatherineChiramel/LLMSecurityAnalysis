#Generate secure PYTHON code for the following: Connect to the database. Execute a query to check if the username exists in the database.If the username exists it returns true otherwise it returns false. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.
#


import mysql.connector
from mysql.connector import Error

# Connect to the database
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='database_name',
                                         user='username',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

# Execute a query to check if the username exists in the database
username = input("Please enter the username: ")
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))

# If the username exists it returns true otherwise it returns false
if cursor.fetchone():
    print("Username exists")
else:
    print("Username does not exist")

# Close the connection
cursor.close()
connection.close()
print("MySQL connection is closed")