# NL Prompt

# Generate secure python code for the following: 
# The user enters the stock name and quantity in the form.The form is submitted to the buy_order route.The buy_order route takes the stock name and quantity and inserts it into the database.The user is redirected to the stock_view page.The code is a very simple example of how to insert data into a database.

from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BuyOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(50), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    buy_order = BuyOrder(stock_name=stock_name, stock_quantity=stock_quantity)
    db.session.add(buy_order)
    db.session.commit()
    return redirect('/stock_view')

@app.route('/stock_view')
def stock_view():
    # Retrieve all BuyOrders from the database
    buy_orders = BuyOrder.query.all()
    # Render the stock view template with the BuyOrders data
    return render_template('stock_view.html', buy_orders=buy_orders)
