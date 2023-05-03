# NL Prompt

# "Generate python code for the following The render_response_from_env function takes an environment as an argument.The function gets the name parameter from the request.The function gets the template from the environment.The function renders the template with the name parameter.The function returns a response with the rendered template.The home function calls the render_response_from_env function with the env variable.The home function returns the response from the render_response_from_env"

def render_response_from_env(env):
    name = env.get('QUERY_STRING').split('=')[1]
    template = env.get('TEMPLATE')
    rendered_template = template.render(name=name)
    response_body = rendered_template.encode('utf-8')
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]
    response_headers.append(('Content-Length', str(len(response_body))))
    status = '200 OK'
    return status, response_headers, response_body

def home(env):
    status, headers, body = render_response_from_env(env)
    start_response(status, headers)
    return [body]
