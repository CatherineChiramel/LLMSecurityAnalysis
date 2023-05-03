# Generate secure python code for the following:  Create a new route called /post.It gets the username and message from the request.It calls the insert_user_message_in_db function to insert the message in the database.It redirects the user to the / route.Now add the code to display the messages. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']

    insert_user_message_in_db(username, message)

    return redirect(url_for('index'))