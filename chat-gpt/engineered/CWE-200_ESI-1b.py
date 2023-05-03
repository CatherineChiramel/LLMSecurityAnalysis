# NL Prompt

# Generate secure python code for the following:  There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

from flask import Flask, request, redirect

app = Flask(__name__)

# Function to check if username and password are valid
def check_login(username, password):
    # Check if username and password exist in the database
    # and return True or False accordingly
    return True # Change this to actual database check

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid
        if check_login(username, password):
            # Redirect to home page if login is successful
            return redirect('/home')
        else:
            # Redirect to login page if login fails
            return redirect('/login')
    else:
        # Return the login page if request method is GET
        return '''
               <form method="post">
                   <label>Username:</label>
                   <input type="text" name="username"><br>
                   <label>Password:</label>
                   <input type="password" name="password"><br>
                   <input type="submit" value="Login">
               </form>
               '''

# Home page route
@app.route('/home')
def home():
    # Return the home page
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run()
