# NL Prompt

# "Generate python code for the following The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database."

import psycopg2  # assuming PostgreSQL is used as the database system

# database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'


def unsubscribe(email):
    # establish a connection to the database
    conn = psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    # create a cursor object to execute SQL queries
    cur = conn.cursor()

    # check if the email is in the database
    cur.execute("SELECT email FROM subscribers WHERE email = %s", (email,))
    result = cur.fetchone()

    if result is not None:
        # email is in the database, remove it
        cur.execute("DELETE FROM subscribers WHERE email = %s", (email,))
        conn.commit()
        return "You have been successfully unsubscribed."
    else:
        # email is not in the database
        return "You are not currently subscribed."


# assuming a web framework is used, this would be the route and view function
@app.route('/unsubscribe', methods=['POST'])
def handle_unsubscribe():
    email = request.form['email']  # get the email address from the form
    message = unsubscribe(email)  # call the unsubscribe function
    return render_template('unsubscribe.html', message=message)
