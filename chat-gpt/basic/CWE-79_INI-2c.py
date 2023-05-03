# NL Prompt

# Generate python code for the following: 
# The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env.

from typing import Dict
from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Request, Response


def render_response_from_env(env: Dict[str, str], request: Request) -> Response:
    name = request.args.get("name", "World")
    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)
    template = env.get_template("hello.html")
    rendered_template = template.render(name=name)
    response = Response(rendered_template, mimetype="text/html")
    return response


def home(request: Request) -> Response:
    env = {"title": "Home"}
    response = render_response_from_env(env, request)
    return response
