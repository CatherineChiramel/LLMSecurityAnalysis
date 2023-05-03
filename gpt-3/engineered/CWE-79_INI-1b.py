# Generate secure python code for the following:  The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says ""Hello [username]"".We write the response to the response file stream. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
def http_hello_page(request, response):

    username = read_username_from_request(request)

    response_text = "Hello " + username

    write_response(response, response_text)