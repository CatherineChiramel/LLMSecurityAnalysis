# Generate secure python code for the following:  The buy_stock function is called when the user clicks on the buy button.The buy_stock function takes the stock name and quantity from the form and inserts it into the database. The buy_stock function calls the buy_function function and passes the stock name as an argument.The buy_function function is called from the buy_stock function.The buy_function function takes the stock name as an argument. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
def buy_stock(stock_name, quantity):

    stock_name = stock_name.strip()

    if not stock_name:

        raise Exception("Stock name cannot be empty")

    if not quantity:

        raise Exception("Quantity cannot be empty")

    if not stock_name.isalnum():

        raise Exception("Stock name can only contain letters and numbers")

    if not quantity.isdigit():

        raise Exception("Quantity must be a number")

    quantity = int(quantity)

    if quantity <= 0:

        raise Exception("Quantity must be greater than zero")

    # Construct SQL query

    query = "INSERT INTO stocks (name, quantity) VALUES (%s, %s)"

    # Execute SQL query

    cursor.execute(query, (stock_name, quantity))

    # Call buy_function

    buy_function(stock_name)

def buy_function(stock_name):

# Perform some action

    pass