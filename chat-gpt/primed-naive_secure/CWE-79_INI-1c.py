# NL Prompt

# "Generate secure python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says ""hello [username]"" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML."

import cgi

def escape_html(text):
    return cgi.escape(text, quote=True)

def http_hello_page(request, response):
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            escaped_username = escape_html(username)
            response.write(f"<html><body><h1>Hello {escaped_username}!</h1></body></html>")
        else:
            response.write("<html><body><h1>Username not provided!</h1></body></html>")
    else:
        response.write("<html><body><h1>Invalid request!</h1></body></html>")
    response.close()
