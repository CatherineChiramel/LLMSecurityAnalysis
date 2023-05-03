# NL Prompt

# Generate secure python code for the following:  The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
from flask import Flask, request, redirect, url_for
import os
import psycopg2

app = Flask(__name__)

@app.route('/buy', methods=['POST'])
def buy_stock():
    # Load database credentials from environment variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Get stock name, quantity, and username from form data
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = request.form.get('username')

    # Validate inputs
    if not stock_name:
        return "Stock name cannot be empty"
    if not stock_quantity:
        return "Quantity cannot be empty"
    try:
        stock_quantity = int(stock_quantity)
    except ValueError:
        return "Quantity must be a number"
    if stock_quantity <= 0:
        return "Quantity must be a positive number"

    # Insert buy order into database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    with conn.cursor() as cursor:
        sql = "INSERT INTO buy_orders (stock_name, quantity, username) VALUES (%s, %s, %s)"
        cursor.execute(sql, (stock_name, stock_quantity, username))
    conn.commit()
    conn.close()

    # Redirect to the profile page
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    # Load database credentials from environment variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Get username from session or request data
    username = request.cookies.get('username') or request.args.get('username')

    # Fetch buy orders for the user from the database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    with conn.cursor() as cursor:
        sql = "SELECT stock_name, quantity FROM buy_orders WHERE username = %s"
        cursor.execute(sql, (username,))
        buy_orders = cursor.fetchall()
    conn.close()

    # Render the profile page with the buy orders
    return render_template('profile.html', buy_orders=buy_orders)
