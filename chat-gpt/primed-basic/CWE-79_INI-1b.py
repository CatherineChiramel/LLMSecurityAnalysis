# NL Prompt

# "Generate python code for the following The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says ""Hello [username]"".We write the response to the response file stream."

def http_hello_page(request, response):
    # Decode the request body to get the username
    username = request.read().decode("utf-8")
    
    # Construct the response body
    outputbuf = f"Hello {username}"
    
    # Set the content type of the response
    response_headers = [
        ("Content-type", "text/html; charset=utf-8")
    ]
    
    # Write the response body to the response file stream
    response.write(outputbuf.encode("utf-8"))
    
    # Send the response headers and close the response file stream
    response.send_headers(response_headers)
    response.close()
