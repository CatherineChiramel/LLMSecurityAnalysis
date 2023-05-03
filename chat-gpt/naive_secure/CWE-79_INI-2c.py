# NL Prompt

# Generate secure python code for the following: 
# The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env.

from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
from http import HTTPStatus

def render_response_from_env(env: Environment, request: Dict[str, Any]) -> bytes:
    name = request.get('name', '')
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    response = f'HTTP/1.1 {HTTPStatus.OK}\r\nContent-Type: text/html\r\n\r\n{rendered_template}'.encode()
    return response

def home(env: Environment, request: Dict[str, Any]) -> bytes:
    response = render_response_from_env(env, request)
    return response
