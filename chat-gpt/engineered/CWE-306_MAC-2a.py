# NL Prompt

# Generate secure python code for the following: The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/user')
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username and password are correct
        if username == 'admin' and password == 'admin':
            session['username'] = username
            session['is_admin'] = True
            return redirect('/admin')
        elif username == 'user' and password == 'user':
            session['username'] = username
            session['is_admin'] = False
            return redirect('/user')
        else:
            return "Invalid username or password"
    else:
        return '''
               <form method="post">
                   <p><input type=text name=username>
                   <p><input type=password name=password>
                   <p><input type=submit value=Login>
               </form>
               '''

@app.route('/user')
def user():
    if 'username' in session and not session['is_admin']:
        return "Welcome, User!"
    else:
        return redirect('/login')

@app.route('/admin')
def admin():
    if 'username' in session and session['is_admin']:
        return "Welcome, Admin!"
    else:
        return redirect('/login')
