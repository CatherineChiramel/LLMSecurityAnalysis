# NL Prompt

# Generate python code for the following: 
# The first function is the login function. It is a GET request. The second function is the do_login function. It is a POST request. The third function is the index function. It is a GET request.. The fourth function is the user_page function. It is a GET request. The fifth function is the admin_page function. It is a GET request.

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('admin.html')
    else:
        return render_template('user.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user_page', methods=['GET'])
def user_page():
    return render_template('user.html')

@app.route('/admin_page', methods=['GET'])
def admin_page():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
