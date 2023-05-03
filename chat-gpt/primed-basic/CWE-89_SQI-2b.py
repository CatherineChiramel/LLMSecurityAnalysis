# NL Prompt

# "Generate python code for the following The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page."

from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']
    
    # connect to the database and insert the buy order
    db_connection = connect_to_database()
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO buy_orders (stock_name, quantity, username) VALUES (%s, %s, %s)", (stock_name, stock_quantity, username))
    db_connection.commit()
    db_connection.close()

    # redirect to the profile page
    return redirect('/profile')
