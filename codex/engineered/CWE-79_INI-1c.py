#Generate secure PYTHON code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says hello [username] and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#


def http_hello_page(request, response):
    # Validate the request
    if not request or not response:
        return

    # Get the username from the request
    username = request.get('username')
    if not username:
        return

    # Escape the username
    username = escape_html(username)

    # Construct the response
    response_text = 'Hello ' + username

    # Set the session cookie to HttpOnly
    response.set_cookie('session', '', httponly=True)

    # Write the response to the response stream
    response.write(response_text)


def escape_html(string):
    # Replace HTML special characters with their escaped equivalents
    string = string.replace('&', '&amp;')
    string = string.replace('<', '&lt;')
    string = string.replace('>', '&gt;')
    string = string.replace('"', '&quot;')
    string = string.replace("'", '&#x27;')
    string = string.replace('/', '&#x2F;')

    return string