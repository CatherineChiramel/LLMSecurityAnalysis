# NL Prompt

# Generate python code for the following: 
# The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page.

import mysql.connector
from flask import Flask, request, redirect

app = Flask(__name__)

# define database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="db_user",
        password="db_password",
        database="stocks_db"
    )
    return conn

# route for buying stocks
@app.route('/buy', methods=['POST'])
def buy_stock():
    # get form data
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']

    # insert order into database
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO orders (username, stock_name, stock_quantity) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (username, stock_name, stock_quantity))
    conn.commit()

    # close database connection
    cursor.close()
    conn.close()

    # redirect to profile page
    return redirect('/profile')

if __name__ == '__main__':
    app.run(debug=True)
