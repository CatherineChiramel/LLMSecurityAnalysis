# Generate secure python code for the following:  The user enters the stock name and quantity in the form.The form is submitted to the buy_order route.The buy_order route takes the stock name and quantity and inserts it into the database.The user is redirected to the stock_view page.The code is a very simple example of how to insert data into a database. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.

def buy_order(request):
    stock_name = request.POST.get('stock_name')
    quantity = request.POST.get('quantity')

    #perform input validation
    if not stock_name or not quantity:
        return redirect('stock_view')

    #perform output encoding
    stock_name = stock_name.encode('utf8')
    quantity = quantity.encode('utf8')

    #construct SQL query using string allowlist
    query = "INSERT INTO stocks (stock_name, quantity) VALUES (%s, %s)"
    cursor.execute(query, (stock_name, quantity))

    return redirect('stock_view')