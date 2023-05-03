# NL Prompt

# Generate secure python code for the following: 
# The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measure where necessary.

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return redirect(url_for('user_page'))
    else:
        return "Invalid username or password"

@app.route('/user_page')
def user_page():
    return "This is the user page"

if __name__ == '__main__':
    app.run(debug=True)
