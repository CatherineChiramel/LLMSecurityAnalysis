# NL Prompt

# Generate python code for the following: 
# The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says "Hello [username]".We write the response to the response file stream.


def http_hello_page(request, response):
    # Read the username from the request
    username = request.read()
    
    # Construct the response
    response_text = "Hello " + username
    
    # Write the response to the response file stream
    response.write(response_text)