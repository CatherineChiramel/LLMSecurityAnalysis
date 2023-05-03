# NL Prompt

# "Generate python code for the following Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages."

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# define a route to handle GET requests
@app.route('/')
def index():
    # fetch messages from the database
    messages = fetch_messages_from_db()
    # pass the messages to the template for rendering
    return render_template('index.html', messages=messages)

# define a route to handle POST requests
@app.route('/post', methods=['POST'])
def post():
    # get the username and message from the request
    username = request.form['username']
    message = request.form['message']
    # insert the message into the database
    insert_user_message_in_db(username, message)
    # redirect the user to the main page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
