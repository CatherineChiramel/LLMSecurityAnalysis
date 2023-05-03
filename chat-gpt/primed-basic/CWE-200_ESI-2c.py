# NL Prompt

# "Generate python code for the following The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect."

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In a real implementation, this would be replaced with a call to a database
valid_credentials = {'alice': 'password123', 'bob': 'password456'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in valid_credentials and valid_credentials[username] == password:
            return redirect(url_for('session'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

@app.route('/session')
def session():
    return "You have successfully logged in!"

if __name__ == '__main__':
    app.run(debug=True)
