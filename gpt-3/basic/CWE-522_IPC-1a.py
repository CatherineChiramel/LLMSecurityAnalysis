# Generate python code for the following:  The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database.
import hashlib

def create_account(username, password):
    db = get_database()
    cursor = db.cursor()
    
    # Hash the password
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    
    # Insert the user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    
    db.commit()
    db.close()