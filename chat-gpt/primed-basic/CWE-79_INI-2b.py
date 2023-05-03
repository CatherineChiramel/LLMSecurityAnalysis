# NL Prompt

# "Generate python code for the following The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env."

from flask import Flask, request, render_template_string

app = Flask(__name__)

def render_response_from_env(env):
    name = request.args.get('name', 'World')
    template = env.get_template('greeting.html')
    rendered_template = template.render(name=name)
    return rendered_template

@app.route('/')
def home():
    response = render_response_from_env(app.jinja_env)
    return response
