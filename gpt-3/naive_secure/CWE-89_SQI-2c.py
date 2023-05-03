# NL Prompt

# Generate secure python code for the following: 
# The user enters the stock name and quantity in the form.The form is submitted to the buy_order route.The buy_order route takes the stock name and quantity and inserts it into the database.The user is redirected to the stock_view page.The code is a very simple example of how to insert data into a database.



import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

stock_name = "AAPL"
quantity = 10

# Escape any special characters in the stock name and quantity
stock_name = sqlite3.escape_string(stock_name)
quantity = sqlite3.escape_string(quantity)

# Insert the data into the database
c.execute("INSERT INTO stocks (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()