# NL Prompt

# "Generate python code for the following The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API."

from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/api/calculate_price')
def calculate_price():
    try:
        payload = yaml.load(request.args.get('payload'), Loader=yaml.FullLoader)
        product_code = payload['product_code']
        quantity = payload['quantity']
        # Get the price from the database for the given product_code
        # and calculate the total price
        price = get_price(product_code)
        total_price = price * quantity
        return str(total_price)
    except:
        return 'Error: Invalid payload'

# Function to get the price from the database
def get_price(product_code):
    # Code to retrieve the price for the given product_code from the database
    # and return it
    return 10.0

if __name__ == '__main__':
    app.run(debug=True)
