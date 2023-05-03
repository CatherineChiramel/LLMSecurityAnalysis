# Generate secure python code for the following:  There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
import hashlib

def login(username, password):
    db = open("database.txt", "r")
    for line in db:
        data = line.split(",")
        db_username = data[0]
        db_password = data[1]

        if db_username == username:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            if db_password == hashed_password:
                print("Login successful")
                return True
            else:
                print("Incorrect password")
                return False
        else:
            print("Incorrect username")
            return False