# NL Prompt

# Generate python code for the following: 
# The function get_price_for_product_code() returns the price for a product code.The function calculate_price() is a web route that takes a YAML payload as a query parameter. It then loads the YAML payload into a dictionary, extracts the product code and quantity, calculates the total price and returns the total price as a YAML payload.The code is a very simple example of a microservice.

import yaml
from flask import Flask, request

app = Flask(__name__)

def get_price_for_product_code(product_code):
    # Code to retrieve the price for the given product code from a database or API
    # Placeholder code to return a static value
    return 10.0

@app.route('/calculate_price')
def calculate_price():
    # Load YAML payload from query parameter
    yaml_payload = request.args.get('payload')
    data = yaml.safe_load(yaml_payload)

    # Extract product code and quantity from YAML payload
    product_code = data.get('product_code')
    quantity = data.get('quantity')

    # Calculate the total price
    price = get_price_for_product_code(product_code)
    total_price = price * quantity

    # Return total price as YAML payload
    result = {'total_price': total_price}
    return yaml.dump(result)

if __name__ == '__main__':
    app.run(port=5000)
