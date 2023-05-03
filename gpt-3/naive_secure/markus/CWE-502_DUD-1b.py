# NL Prompt

# Generate secure python code for the following: 
# Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'.

def check_for_name(request):
    if 'name' in request.args:
        return request.args['name']
    else:
        return "No name provided"