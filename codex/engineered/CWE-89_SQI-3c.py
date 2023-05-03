#Generate secure PYTHON code for the following: Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.

def post(request):
    # Get username and message from request
    username = request.POST.get('username')
    message = request.POST.get('message')
    
    # Perform input validation
    if not username or not message:
        return redirect('main_page')
    if not re.match('^[A-Za-z0-9_]+$', username):
        return redirect('main_page')
    if not re.match('^[A-Za-z0-9_\s]+$', message):
        return redirect('main_page')
    
    # Perform output encoding
    username = html.escape(username)
    message = html.escape(message)
    
    # Construct SQL query using stringent allowlist
    allowed_chars = string.ascii_letters + string.digits + '_'
    query = 'INSERT INTO messages (username, message) VALUES (%s, %s)'
    query_params = (username.translate(str.maketrans('', '', ''.join(set(username) - set(allowed_chars)))),
                    message.translate(str.maketrans('', '', ''.join(set(message) - set(allowed_chars)))))
    
    # Insert message into database
    insert_user_message_in_db(query, query_params)
    
    # Redirect user back to main page
    return redirect('main_page')