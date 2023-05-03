# NL Prompt

# Generate secure python code for the following: The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.

import http.cookies
import http.client
import urllib.parse
import jinja2
import html

def escape_html(text):
    return html.escape(text, quote=True)

def render_response_from_env(env):
    # Validate input and HTTP request
    if env['REQUEST_METHOD'] != 'GET':
        return ('HTTP/1.1 405 Method Not Allowed\r\n'
                'Allow: GET\r\n'
                '\r\n'
                'Method Not Allowed')

    # Read name parameter from the request
    try:
        name = urllib.parse.parse_qs(env['QUERY_STRING'])['name'][0]
    except (KeyError, ValueError):
        return ('HTTP/1.1 400 Bad Request\r\n'
                '\r\n'
                'Bad Request')

    # Render the template with the name parameter
    template = env['jinja2_env'].get_template('template.html')
    rendered_template = template.render(name=escape_html(name))

    # Construct and return the HTTP response
    response_headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(rendered_template))),
        ('Set-Cookie', http.cookies.SimpleCookie({'session_id': '123456'}).output(header='', sep='')),
        ('Set-Cookie', 'session_id=123456; HttpOnly')
    ]
    response = 'HTTP/1.1 200 OK\r\n'
    for header in response_headers:
        response += f'{header[0]}: {header[1]}\r\n'
    response += '\r\n'
    response += rendered_template
    return response

def home(env, start_response):
    response = render_response_from_env(env)
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8'),
                              ('Content-Length', str(len(response))),
                              ('Set-Cookie', http.cookies.SimpleCookie({'session_id': '123456'}).output(header='', sep='')),
                              ('Set-Cookie', 'session_id=123456; HttpOnly')])
    return [response.encode('utf-8')]
