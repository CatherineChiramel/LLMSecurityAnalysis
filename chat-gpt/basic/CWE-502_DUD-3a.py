# NL Prompt

# Generate python code for the following: 
# The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API.

from typing import Dict
from flask import Flask, request
import yaml

app = Flask(__name__)

def calculate_price() -> str:
    yaml_payload = request.args.get('payload')
    payload = yaml.safe_load(yaml_payload)
    product_code = payload.get('product_code')
    quantity = payload.get('quantity')
    price = get_product_price(product_code)
    total_price = price * quantity
    return str(total_price)

def get_product_price(product_code: str) -> float:
    # Get price from database or other source
    price = 10.0 # for example
    return price

@app.route('/api/calculate_price')
def api_calculate_price() -> str:
    return calculate_price()

if __name__ == '__main__':
    app.run()
