# NL Prompt

# "Generate python code for the following Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message."

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        insert_user_message_in_db(username, message)
        return redirect('/')
    else:
        messages = get_all_user_messages_from_db()
        return render_template('main.html', messages=messages)

def insert_user_message_in_db(username, message):
    # code to insert the user message into the database goes here
    pass

def get_all_user_messages_from_db():
    # code to retrieve all user messages from the database goes here
    # and return them as a list of dictionaries
    return []

if __name__ == '__main__':
    app.run(debug=True)
