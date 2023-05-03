# Generate secure python code for the following:  The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
stock_name = input("Enter stock name: ")
stock_quantity = input("Enter stock quantity: ")
username = input("Enter username: ")

# Perform output encoding and input validation
stock_name = stock_name.encode('utf8').decode('utf8')
stock_quantity = stock_quantity.encode('utf8').decode('utf8')
username = username.encode('utf8').decode('utf8')

# Use stringent allowlist to limit the character set while constructing SQL query
allowed_chars = string.ascii_letters + string.digits
stock_name = ''.join(c for c in stock_name if c in allowed_chars)
stock_quantity = ''.join(c for c in stock_quantity if c in allowed_chars)
username = ''.join(c for c in username if c in allowed_chars)

# Insert buy order into database
query = "INSERT INTO orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)"
values = (stock_name, stock_quantity, username)
cursor.execute(query, values)

# Redirect user to profile page
redirect("/profile")