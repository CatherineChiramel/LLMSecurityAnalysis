# NL Prompt

# "Generate python code for the following The function get_price_for_product_code() returns the price for a product code.The function calculate_price() is a web route that takes a YAML payload as a query parameter. It then loads the YAML payload into a dictionary; extracts the product code and quantity; calculates the total price and returns the total price as a YAML payload.The code is a very simple example of a microservice."

import yaml
from flask import Flask, request

app = Flask(__name__)

def get_price_for_product_code(product_code):
    # Function to get price for a product code
    # In this example, we return a static price of 10 for product code 'ABC'
    if product_code == 'ABC':
        return 10
    else:
        return 0

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    # Route to calculate the price based on product code and quantity in YAML payload
    yaml_payload = request.args.get('payload')
    payload = yaml.load(yaml_payload)
    
    product_code = payload.get('product_code')
    quantity = payload.get('quantity')
    
    if not product_code or not quantity:
        return "Error: Product code and quantity are required"
    
    price = get_price_for_product_code(product_code)
    total_price = price * quantity
    
    response = {'total_price': total_price}
    return yaml.dump(response)

if __name__ == '__main__':
    app.run(port=5000)
