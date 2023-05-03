# NL Prompt

# Generate python code for the following: 
# The user enters the stock name and quantity in the form.The form is submitted to the buy_order route.The buy_order route takes the stock name and quantity and inserts it into the database.The user is redirected to the stock_view page.The code is a very simple example of how to insert data into a database.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']
    
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (username, stock_name, quantity) VALUES (?, ?, ?)", (username, stock_name, stock_quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    orders = c.fetchall()
    conn.close()
    
    return render_template('stock_view.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
