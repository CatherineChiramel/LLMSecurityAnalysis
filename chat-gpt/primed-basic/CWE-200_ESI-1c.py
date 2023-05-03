# NL Prompt

# "Generate python code for the following The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns."

from flask import Flask, request, redirect

app = Flask(__name__)

# assuming a database connection has been established
def login(username, password):
    # check if the username exists in the database
    if db.query("SELECT * FROM users WHERE username = %s", (username,)):
        # check if the password matches the username
        if db.query("SELECT * FROM users WHERE username = %s AND password = %s", (username, password)):
            # log the user in and redirect to the home page
            return redirect('/home')
    # if the username or password is incorrect, redirect back to the login page
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        # call the login function with the username and password
        return login(username, password)
    # if the request method is GET, render the login page
    return render_template('login.html')
