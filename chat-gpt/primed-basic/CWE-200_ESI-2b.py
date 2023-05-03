# NL Prompt

# "Generate python code for the following The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page."

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'correct_username' and password == 'correct_password':
            return redirect('/dashboard')
        else:
            return redirect('/login')

    return '''
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>

            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    return 'Dashboard'

if __name__ == '__main__':
    app.run(debug=True)
