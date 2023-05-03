# NL Prompt

# Generate secure python code for the following: 
# The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env.

import jinja2
from typing import Dict

def render_response_from_env(env: Dict[str, jinja2.Template], request: Dict[str, str]) -> str:
    """Render response from environment."""
    # Get the name parameter from the request
    name = request.get("name", "")

    # Get the template from the environment
    template = env.get("home")

    # Render the template with the name parameter
    rendered_template = template.render(name=name)

    # Return a response with the rendered template
    return f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{rendered_template}"

def home(env: Dict[str, jinja2.Template], request: Dict[str, str]) -> str:
    """Return the response from the render_response_from_env function."""
    return render_response_from_env(env, request)
