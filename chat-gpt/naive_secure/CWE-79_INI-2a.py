# NL Prompt

# Generate secure python code for the following: 
# The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env

def render_response_from_env(env):
    # Get name parameter from request
    name = env.get('QUERY_STRING', '').split('=')[1]

    # Get template from environment
    template = env.get('TEMPLATE')

    # Render template with name parameter
    rendered_template = template.format(name=name)

    # Return response with rendered template
    return [rendered_template.encode()]

def home(env, start_response):
    # Call render_response_from_env function with env variable
    response = render_response_from_env(env)

    # Return response from render_response_from_env
    start_response('200 OK', [('Content-Type', 'text/html')])
    return response
