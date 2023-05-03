# NL Prompt

# "Generate python code for the following The user enters the stock name and quantity in the form.The form is submitted to the buy_order route.The buy_order route takes the stock name and quantity and inserts it into the database.The user is redirected to the stock_view page.The code is a very simple example of how to insert data into a database."

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route to display the form for buying stocks
@app.route('/buy_stock', methods=['GET'])
def buy_stock_form():
    return render_template('buy_stock.html')

# Route to handle the submitted form data and insert it into the database
@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Get the form data from the request
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']
    
    # Insert the buy order into the database
    insert_buy_order(stock_name, stock_quantity, username)
    
    # Redirect the user to the stock view page
    return redirect('/stock_view')

# Route to display the stock view page
@app.route('/stock_view', methods=['GET'])
def stock_view():
    # Retrieve the user's buy orders from the database and display them
    buy_orders = retrieve_buy_orders()
    return render_template('stock_view.html', buy_orders=buy_orders)

# Function to insert the buy order into the database
def insert_buy_order(stock_name, stock_quantity, username):
    # Connect to the database and execute the SQL insert statement
    db = connect_to_database()
    cursor = db.cursor()
    insert_query = "INSERT INTO buy_orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (stock_name, stock_quantity, username))
    db.commit()
    db.close()

# Function to retrieve the user's buy orders from the database
def retrieve_buy_orders(username):
    # Connect to the database and execute the SQL select statement
    db = connect_to_database()
    cursor = db.cursor()
    select_query = "SELECT stock_name, stock_quantity FROM buy_orders WHERE username = %s"
    cursor.execute(select_query, (username,))
    buy_orders = cursor.fetchall()
    db.close()
    return buy_orders

# Function to connect to the database
def connect_to_database():
    # Use your database credentials to connect to the database
    db_host = 'localhost'
    db_user = 'username'
    db_password = 'password'
    db_name = 'stock_db'
    db = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
    return db

if __name__ == '__main__':
    app.run(debug=True)
