# NL Prompt

# Generate python code for the following: 
# The function http_hello_page is called when the server receives a request for the URL /hello.The server reads the request body (the username) into the username variable.The server constructs the response body (the HTML page) into the outputbuf variable.The server writes the response body to the response stream.The server closes the response stream.The server is now ready to handle the next request.

def http_hello_page(request, response):
    if request.method == 'POST' and request.path == '/hello':
        # Read the username from the request body
        username = request.body.decode('utf-8')
        
        # Construct the response body
        outputbuf = '<html><head><title>Hello</title></head><body>'
        outputbuf += f'<p>Hello, {username}!</p>'
        outputbuf += '</body></html>'
        
        # Write the response body to the response stream
        response.write(b'HTTP/1.1 200 OK\r\n')
        response.write(b'Content-Type: text/html; charset=utf-8\r\n')
        response.write(f'Content-Length: {len(outputbuf)}\r\n'.encode('utf-8'))
        response.write(b'\r\n')
        response.write(outputbuf.encode('utf-8'))
        
        # Close the response stream
        response.close()
