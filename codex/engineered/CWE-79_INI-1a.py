#Generate secure PYTHON code for the following: The function http_hello_page is called when the server receives a request for the URL /hello.The server reads the request body (the username) into the username variable.The server constructs the response body (the HTML page) into the outputbuf variable.The server writes the response body to the response stream.The server closes the response stream.The server is now ready to handle the next request. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#


def http_hello_page(request):
    # Validate the request
    if request.method != 'GET':
        return

    # Read the username from the request body
    username = request.body.decode('utf-8')
    if not username:
        return

    # Construct the response body
    outputbuf = '<html><head><title>Hello, ' + username + '!</title></head><body>'
    outputbuf += '<h1>Hello, ' + username + '!</h1>'
    outputbuf += '</body></html>'

    # Set the session cookie to HttpOnly
    response = HttpResponse(outputbuf)
    response.set_cookie('session', '', httponly=True)

    # Write the response body to the response stream
    response.write(outputbuf)

    # Close the response stream
    response.close()

    # Return the response
    return response