# NL Prompt

# "Generate secure python code for the following Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages."

from flask import Flask, request, redirect

app = Flask(__name__)

# connect to the database securely
# ...

@app.route('/post', methods=['POST'])
def post():
    # get the username and message from the request form
    username = request.form.get('username')
    message = request.form.get('message')

    # sanitize and validate inputs
    if not username or not message:
        # handle error
        return redirect('/error')
    
    # insert message into the database
    db = get_db()  # get database connection
    cursor = db.cursor()
    cursor.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))
    db.commit()
    
    # redirect the user to the main page
    return redirect('/')
    
@app.route('/')
def main():
    # fetch messages from the database and display them
    # ...
    return render_template('main.html', messages=messages)
