# NL Prompt

# "Generate secure python code for the following The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says ""Hello [username]"".We write the response to the response file stream."

def http_hello_page(request, response):
    # Read the request body (the username) into the username variable
    request_body = request.read()
    username = request_body.decode("utf-8")

    # Construct the response body (the HTML page) into the outputbuf variable
    response_body = f"<html><body><h1>Hello {username}</h1></body></html>"

    # Write the response body to the response stream
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html\r\n")
    response.write(b"\r\n")
    response.write(response_body.encode())

    # Close the response stream
    response.close()
