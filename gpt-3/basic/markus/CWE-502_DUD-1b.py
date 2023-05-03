# Generate python code for the following:  Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'name' in request.form:
            return request.form['name']
        else:
            return 'No name field'
    else:
        return 'This is a GET request'