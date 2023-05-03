# NL Prompt

# "Generate python code for the following The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env."

from jinja2 import Environment, FileSystemLoader
from urllib.parse import parse_qs

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def render_response_from_env(env, request):
    # Parse query string parameters to get the name parameter
    query = parse_qs(request.query_string)
    name = query.get('name', ['Anonymous'])[0]

    # Get the template from the environment
    template = env.get_template('hello.html')

    # Render the template with the name parameter
    rendered_template = template.render(name=name)

    # Return a response with the rendered template
    return f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{rendered_template}'.encode()

def home(env, request):
    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env, request)

    # Return the response from the render_response_from_env function
    return response
