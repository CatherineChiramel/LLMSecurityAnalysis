#Generate secure PYTHON code for the following: The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist to limit the character set while constructing SQL query. Use additional security measures where necessary.
#


# Import necessary modules
import re
import sqlite3
from flask import request, redirect, session

# Get the stock name and quantity from the form
stock_name = request.form.get('stock_name')
stock_quantity = request.form.get('stock_quantity')

# Get the username from the session
username = session.get('username')

# Perform input validation
if not re.match('^[A-Za-z0-9_]+$', stock_name):
    raise ValueError('Invalid stock name')

if not re.match('^[0-9]+$', stock_quantity):
    raise ValueError('Invalid stock quantity')

# Connect to the database
conn = sqlite3.connect('database.db')

# Construct the SQL query using stringent allowlist
allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
query = 'INSERT INTO stocks (username, stock_name, stock_quantity) VALUES (?, ?, ?)'
query = ''.join(c for c in query if c in allowed_chars)

# Execute the query
cursor = conn.cursor()
cursor.execute(query, (username, stock_name, stock_quantity))
conn.commit()

# Redirect the user to the profile page
return redirect('/profile')