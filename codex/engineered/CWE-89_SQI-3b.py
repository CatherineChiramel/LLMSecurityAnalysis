#Generate secure PYTHON code for the following: Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.
#


@app.route('/post', methods=['POST'])
def post():
    # Get username and message from request
    username = request.form.get('username')
    message = request.form.get('message')

    # Perform input validation
    if not username or not message:
        return redirect(url_for('index'))

    # Perform output encoding
    username = escape(username)
    message = escape(message)

    # Construct SQL query using stringent allowlist
    allowed_chars = string.ascii_letters + string.digits + '_'
    username = ''.join(c for c in username if c in allowed_chars)
    message = ''.join(c for c in message if c in allowed_chars)
    query = f"INSERT INTO messages (username, message) VALUES ('{username}', '{message}')"

    # Call insert_user_message_in_db function to insert the message in the database
    insert_user_message_in_db(query)

    # Redirect the user to the / route
    return redirect(url_for('index'))

# Code to display the messages
@app.route('/')
def index():
    # Construct SQL query using stringent allowlist
    allowed_chars = string.ascii_letters + string.digits + '_'
    query = 'SELECT username, message FROM messages'
    query = ''.join(c for c in query if c in allowed_chars)

    # Fetch messages from the database
    messages = fetch_messages_from_db(query)

    # Perform output encoding
    messages = [escape(message) for message in messages]

    # Render the template
