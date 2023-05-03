# NL Prompt

# Generate secure python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says ""hello [username]"" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
import http.cookies
import http.client
import urllib.parse
import html

def escape_html(text):
    return html.escape(text, quote=True)

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
    hello_message = f'Hello {escape_html(username)}'.encode('utf-8')
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
