# NL Prompt

# Generate secure python code for the following:  The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# create the subscribers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        email TEXT PRIMARY KEY
    )
''')
conn.commit()

# unsubscribe endpoint
@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    # get the email parameter from the request
    email = request.args.get('email')

    # validate email input
    if not email:
        return 'Please provide an email address'

    # check if email is in the database
    cursor.execute('SELECT email FROM subscribers WHERE email = ?', (email,))
    result = cursor.fetchone()

    if not result:
        return 'Email not found in our database'

    # remove email from the database
    cursor.execute('DELETE FROM subscribers WHERE email = ?', (email,))
    conn.commit()

    return 'You have been unsubscribed from our mailing list'

if __name__ == '__main__':
    app.run()


# In this code, we first create a subscribers table in the database to store the email addresses of subscribers. The unsubscribe function then checks if an email parameter was provided in the GET request, and returns an error message if not. We then use a parameterized SQL query to check if the email exists in the database, and return an error message if it does not. If the email is found, we use another parameterized SQL query to delete the email from the database and commit the changes. Finally, we return a success message to the user.