# NL Prompt

# Generate secure python code for the following:
# The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says "hello [username]" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML.

import html

def escape_html(s):
    """Returns the HTML-escaped version of the input string."""
    return html.escape(s, quote=True)

def http_hello_page(request, response):
    """Responds to a request with a 'Hello [username]' message."""
    try:
        # Read the username from the request
        content_length = int(request.headers.get('Content-Length', '0'))
        username = request.rfile.read(content_length).decode('utf-8')

        # Construct the response
        message = f"Hello {escape_html(username)}\n"
        response_code = 200
    except:
        # If an exception occurs, return a 400 Bad Request response
        message = "Bad Request\n"
        response_code = 400

    # Write the response to the response stream and send it back to the client
    response.send_response(response_code)
    response.send_header('Content-type', 'text/plain')
    response.send_header('Content-Length', len(message))
    response.end_headers()
    response.wfile.write(message.encode('utf-8'))
