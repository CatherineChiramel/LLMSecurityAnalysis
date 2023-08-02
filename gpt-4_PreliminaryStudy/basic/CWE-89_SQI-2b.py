# NL Prompt

# Generate python code for the following:  The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page.

from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
config = {
    'user': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'host': 'YOUR_HOST',
    'database': 'YOUR_DATABASE_NAME',
    'raise_on_warnings': True
}


@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    # this can also be obtained from a session if you have authentication
    username = request.form.get('username')

    if not all([stock_name, stock_quantity, username]):
        return "All fields are required!", 400

    try:
        # Connect to the database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = """INSERT INTO orders (username, stock_name, stock_quantity) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (username, stock_name, stock_quantity))

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        return f"Database error: {err}", 500

    # Redirect to the profile page
    return redirect('/profile')


@app.route('/profile')
def profile_page():
    # This is a placeholder function, you should load user-specific data and render it
    return "Welcome to your profile page!"


if __name__ == '__main__':
    app.run(debug=True)
