# NL Prompt

# Generate secure python code for the following: Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.

from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# define function to insert user message in database
def insert_user_message_in_db(username, message):
    # connect to database
    db = pymysql.connect(host='localhost', user='root', password='password', db='my_db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    # prepare SQL query to insert message
    sql = "INSERT INTO messages (username, message) VALUES (%s, %s)"
    data = (username, message)

    # execute query and commit changes to database
    with db.cursor() as cursor:
        cursor.execute(sql, data)
    db.commit()

    # close database connection
    db.close()

# define route for post form
@app.route('/post', methods=['POST'])
def post():
    # get username and message from form
    username = request.form['username']
    message = request.form['message']

    # insert message in database
    insert_user_message_in_db(username, message)

    # redirect user to main page
    return redirect('/')

# define route to display messages
@app.route('/')
def display_messages():
    # connect to database
    db = pymysql.connect(host='localhost', user='root', password='password', db='my_db', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    # prepare SQL query to select messages
    sql = "SELECT username, message FROM messages"

    # execute query
    with db.cursor() as cursor:
        cursor.execute(sql)
        messages = cursor.fetchall()

    # close database connection
    db.close()

    # render template with messages
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
