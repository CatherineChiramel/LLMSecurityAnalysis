# Generate secure python code for the following:  The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.

import hashlib

def create_account(username, password, first_name, last_name, email):
    db = sqlite3.connect('accounts.db')
    c = db.cursor()
    h = hashlib.sha256(password.encode('utf-8')).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    r = c.fetchone()
    if r:
        return 'That username already exists'
    else:
        c.execute('INSERT INTO users VALUES (?,?,?,?,?)', (username, h, first_name, last_name, email))
        db.commit()
        db.close()
        return 'Registration succeeded'