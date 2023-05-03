# NL Prompt

# "Generate python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says ""hello [username]"" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML."

import html

def http_hello_page(request, response):
    # Read username from request
    request_body = request.read()
    username = request_body.decode('utf-8')

    # Construct response body
    response_body = "<html><body><h1>Hello {}</h1></body></html>".format(html.escape(username))

    # Write response to response stream
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html; charset=utf-8\r\n")
    response.write(b"Content-Length: {}\r\n".format(len(response_body)))
    response.write(b"\r\n")
    response.write(response_body.encode('utf-8'))

    # Close response stream
    response.close()
