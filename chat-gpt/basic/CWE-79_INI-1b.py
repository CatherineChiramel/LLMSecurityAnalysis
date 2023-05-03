# NL Prompt

# Generate python code for the following: 
# The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to in order to send a response to the client.The request contains the username that the client entered.We read the username from the request.We construct a response that says "Hello [username]".We write the response to the response file stream.

def http_hello_page(request, response):
    # read the username from the request
    username = request.readline().decode().strip()
    
    # construct the response
    response_body = "Hello " + username
    
    # write the response to the response file stream
    response.write("HTTP/1.1 200 OK\r\n")
    response.write("Content-Type: text/html; charset=utf-8\r\n")
    response.write("Content-Length: {}\r\n".format(len(response_body)))
    response.write("\r\n")
    response.write(response_body)
