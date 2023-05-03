# NL Prompt

# Generate secure python code for the following: 
# The buy_stock function is called when the user clicks on the buy button.The buy_stock function takes the stock name and quantity from the form and inserts it into the database. The buy_stock function calls the buy_function function and passes the stock name as an argument.The buy_function function is called from the buy_stock function.The buy_function function takes the stock name as an argument.


def buy_stock(stock_name, quantity):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO stocks (stock_name, quantity) VALUES (%s, %s)", (stock_name, quantity))
    connection.commit()
    cursor.close()

def buy_function(stock_name):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stocks WHERE stock_name=%s", (stock_name,))
    result = cursor.fetchone()
    connection.commit()
    cursor.close()
    return result