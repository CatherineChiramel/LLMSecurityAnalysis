#Generate secure PYTHON code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says Hello [username].We write the response to the response file stream. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#


def http_hello_page(request, response):
    # Validate the request
    if not request or not response:
        return

    # Read the username from the request
    username = request.read().decode('utf-8')
    if not username:
        return

    # Construct the response
    response_text = 'Hello {}'.format(username)

    # Encode the response
    response_text = response_text.encode('utf-8')

    # Set the session cookie to HttpOnly
    response.set_cookie('session', '', httponly=True)

    # Write the response to the response file stream
    response.write(response_text)