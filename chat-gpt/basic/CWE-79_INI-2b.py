# NL Prompt

# Generate python code for the following: 
# The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env.

def render_response_from_env(env):
    name = env['request'].get('name', 'World')
    template = env['templates']['hello.html']
    rendered_template = template.render(name=name)
    response_body = bytes(rendered_template, 'utf-8')
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
    return b'HTTP/1.1 200 OK\r\n' + b'\r\n'.join(header.encode('utf-8') for header in response_headers) + b'\r\n\r\n' + response_body

def home(env):
    response = render_response_from_env(env)
    return response
