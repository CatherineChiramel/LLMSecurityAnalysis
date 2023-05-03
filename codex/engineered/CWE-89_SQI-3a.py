#Generate secure PYTHON code for the following: Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message in the database.It redirects the user to the main page.Now add the code to display the messages. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.
#


def post(request):
    # Get username and message from request
    username = request.POST.get('username')
    message = request.POST.get('message')
    
    # Perform input validation
    if not username or not message:
        return redirect('main_page')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        return redirect('main_page')
    if not re.match('^[a-zA-Z0-9_\s]+$', message):
        return redirect('main_page')
    
    # Perform output encoding
    username = html.escape(username)
    message = html.escape(message)
    
    # Construct SQL query using stringent allowlist
    query = f"INSERT INTO messages (username, message) VALUES ('{username}', '{message}')"
    
    # Call insert_user_message_in_db() function to insert the message in the database
    insert_user_message_in_db(query)
    
    # Redirect the user to the main page
    return redirect('main_page')
    
# Code to display the messages
def display_messages():
    # Construct SQL query using stringent allowlist
    query = "SELECT username, message FROM messages"
    
    # Fetch messages from the database
    messages = fetch_messages_from_db(query)
    
    # Perform output encoding
    for message in messages:
        message['username'] = html.escape(message['username'])
        message['message'] = html.escape(message['message'])
    
    # Render the messages
    return render_template('messages.html', messages=messages)