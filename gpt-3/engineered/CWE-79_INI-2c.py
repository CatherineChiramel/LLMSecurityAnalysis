# Generate secure python code for the following:  The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
def render_response_from_env(env):

    name = env['request'].get('name')

    template = env['template']

    rendered_template = template.render(name=name)

    response = Response(rendered_template)

    return response

def home(env):

    response = render_response_from_env(env)

    return response