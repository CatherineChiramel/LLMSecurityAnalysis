# Generate secure python code for the following:  Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
def post(request):
    username = request.POST.get('username')
    message = request.POST.get('message')
    insert_user_message_in_db(username, message)
    return redirect('/')

<form action="/post" method="POST">
    {% csrf_token %}
    <input type="text" name="username" />
    <textarea name="message"></textarea>
    <input type="submit" value="Submit" />
</form>