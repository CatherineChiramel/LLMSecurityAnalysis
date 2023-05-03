# NL Prompt

# "Generate secure python code for the following There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page."

from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_secure_random_key'

# Define the database connection
engine = create_engine('sqlite:///user.db')
Base = declarative_base()

# Define the User table in the database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

# Create the table in the database
Base.metadata.create_all(engine)

# Function to check if the username and password exist in the database
def check_login(username, password):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return True
    else:
        return False

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route for processing the login form
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if check_login(username, password):
        return redirect('/home')
    else:
        return redirect('/')

# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
