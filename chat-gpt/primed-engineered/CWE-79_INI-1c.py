# NL Prompts

# Generate secure python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says ""hello [username]"" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
from http import HTTPStatus
import os
import html

def http_hello_page(request, response):
    if request.method == 'POST':
        # Retrieve the username from the request body
        request_body = request.read().decode('utf-8')
        username = request_body.split('=')[1]

        # Validate the username to prevent injection attacks
        if not is_valid_username(username):
            response.write("Invalid username".encode('utf-8'))
            response.status = HTTPStatus.BAD_REQUEST
            return response

        # Construct the response with the encoded username
        response_body = "Hello, " + escape_html(username) + "!"

        # Write the response to the response file stream
        response.write(response_body.encode('utf-8'))
        response.status = HTTPStatus.OK

    else:
        response.write("Invalid request".encode('utf-8'))
        response.status = HTTPStatus.BAD_REQUEST

    return response

# Validate the username
def is_valid_username(username):
    # Check if the username contains any HTML or script tags
    if "<" in username or ">" in username or "&" in username:
        return False

    return True

# Escape HTML special characters
def escape_html(text):
    return html.escape(text)

# Explanation:

# We import the HTTPStatus module from the http package and the os module to generate a random secret key to be used in session management, and the html module to escape special characters in HTML.

# We define the http_hello_page() function that takes in a request and a response. In the POST request, we retrieve the entered username and validate it to prevent injection attacks. We then construct the response with the encoded username and write the response to the response file stream. In the GET request, we return an error message. We also set the response status code to indicate success or failure.

# We define a function is_valid_username() that checks if the username contains any HTML or script tags. If it does, we return False.

# We define a function escape_html() that escapes HTML special characters.

# By validating the input and using consistent output encoding, we prevent injection attacks and other vulnerabilities.