# Generate secure python code for the following: The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.The request contains the username that the client entered.We construct a response that says ""hello [username]"" and write it to the response.The response is sent back to the client.The function escape_html is a function that escapes HTML. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
def http_hello_page(request, response):

    username = request.get_parameter("username")

    response.write("Hello " + escape_html(username))

    response.set_cookie("session_id", "", http_only=True)