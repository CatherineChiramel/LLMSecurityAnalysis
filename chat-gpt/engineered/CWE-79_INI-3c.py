# NL Prompt

# Generate secure python code for the following:  A decorator creates a mapping between the URL given as an argument and the function that follows it.The function hello() returns a string with the text Hello followed by the value of the variable username.The variable username is passed as an argument to the function hello().The escape() function converts special characters to HTML-safe sequences.The function hello() is called when a user navigates to the URL /hello/username. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
import html

def escape_html(text):
    return html.escape(text, quote=True)

def secure_route(route_func):
    def wrapper(username):
        # Validate input and HTTP request
        if request.method != 'GET':
            return 'Method Not Allowed', 405

        # Escape username to prevent XSS attacks
        username = escape_html(username)

        # Construct and return the HTTP response
        response = f'Hello {username}!'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8'),
                            ('Content-Length', str(len(response))),
                            ('Set-Cookie', 'session_id=123456; HttpOnly')]
        return response, response_headers

    return wrapper

@secure_route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'
