# NL Prompt

# Generate python code for the following:
# The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says "hello [username]" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML.

import html

def escape_html(text):
    return html.escape(text, quote=True)

def http_hello_page(request, response):
    username = request.read().decode().strip()
    escaped_username = escape_html(username)
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html\r\n")
    response.write(b"\r\n")
    response.write(b"<html><body>\n")
    response.write(b"<h1>Hello ")
    response.write(escaped_username.encode())
    response.write(b"!</h1>\n")
    response.write(b"</body></html>\n")
    response.close()
