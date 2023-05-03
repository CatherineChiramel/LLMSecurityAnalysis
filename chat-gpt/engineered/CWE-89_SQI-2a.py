# NL Prompt

# Generate secure python code for the following:  The buy_stock function is called when the user clicks on the buy button.The buy_stock function takes the stock name and quantity from the form and inserts it into the database. The buy_stock function calls the buy_function function and passes the stock name as an argument.The buy_function function is called from the buy_stock function.The buy_function function takes the stock name as an argument. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import os
import psycopg2

def buy_stock(stock_name, quantity):
    # Load database credentials from environment variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Create database connection
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Validate inputs
    if not stock_name:
        return "Stock name cannot be empty"
    if not quantity:
        return "Quantity cannot be empty"
    try:
        quantity = int(quantity)
    except ValueError:
        return "Quantity must be a number"
    if quantity <= 0:
        return "Quantity must be a positive number"

    # Insert stock information into database
    with conn.cursor() as cursor:
        sql = "INSERT INTO stock_info (stock_name, quantity) VALUES (%s, %s)"
        cursor.execute(sql, (stock_name, quantity))

    # Call buy_function with stock_name argument
    buy_function(stock_name)

    # Close database connection
    conn.close()

def buy_function(stock_name):
    # Load database credentials from environment variables
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Create database connection
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Execute SQL query to buy stock
    with conn.cursor() as cursor:
        sql = "UPDATE stocks SET quantity = quantity + 1 WHERE stock_name = %s"
        cursor.execute(sql, (stock_name,))

    # Close database connection
    conn.close()
