# NL Prompt

# "Generate secure python code for the following The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page."

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Stock('{self.name}', {self.quantity})"

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found"
    stock = Stock(name=stock_name, quantity=stock_quantity, user_id=user.id)
    db.session.add(stock)
    db.session.commit()
    buy_function(stock_name)
    return redirect('/profile')

@app.route('/profile')
def profile():
    # Authenticate user
    if not is_authenticated(request):
        return redirect('/login')
    # Retrieve user's stocks from the database
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found"
    stocks = Stock.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', stocks=stocks)

def is_authenticated(request):
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return False
    return True

def buy_function(stock_name):
    # perform the buy operation
    pass
