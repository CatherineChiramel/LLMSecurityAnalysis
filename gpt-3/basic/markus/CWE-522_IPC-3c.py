# Generate python code for the following:  The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database.
import bcrypt

username = input("Enter a username: ")
password = input("Enter a password: ")

hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# The following line is vulnerable to SQL injection

sql = "INSERT INTO users (username, password) VALUES ('{}', '{}')".format(username, hashed_password)

# The code should be sanitized as follows:

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"

# The code above is safe from SQL injection.