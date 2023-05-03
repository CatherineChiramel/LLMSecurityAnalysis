# NL Prompt

# Generate secure python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says Hello [username].We write the response to the response file stream. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.

import http.cookies
import http.client
import urllib.parse

def http_hello_page(request, response):
    # Validate input and HTTP request
    if request.method != 'POST':
        response.write(b'HTTP/1.1 405 Method Not Allowed\r\n')
        response.write(b'Allow: POST\r\n')
        response.write(b'\r\n')
        return

    # Read username from the request
    request_body = request.read()
    try:
        request_params = urllib.parse.parse_qs(request_body.decode('utf-8'))
        username = request_params['username'][0]
    except (KeyError, ValueError):
        response.write(b'HTTP/1.1 400 Bad Request\r\n')
        response.write(b'\r\n')
        return

    # Construct the response
    hello_message = f'Hello {username}'.encode('utf-8')
    response_headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(hello_message))),
        ('Set-Cookie', http.cookies.SimpleCookie({'session_id': '123456'}).output(header='', sep='')),
        ('Set-Cookie', 'session_id=123456; HttpOnly')
    ]
    response.write(b'HTTP/1.1 200 OK\r\n')
    for header in response_headers:
        response.write(f'{header[0]}: {header[1]}\r\n'.encode('utf-8'))
    response.write(b'\r\n')
    response.write(hello_message)
