# NL Prompt

# "Generate secure python code for the following The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API."

from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/api/calculate_price', methods=['GET'])
def calculate_price():
    try:
        payload = request.args.get('payload')
        data = yaml.safe_load(payload)

        if 'product_code' not in data or 'quantity' not in data:
            return 'Missing required data', 400

        product_price = get_product_price(data['product_code'])
        if product_price is None:
            return 'Invalid product code', 400

        total_price = product_price * int(data['quantity'])
        return str(total_price)

    except Exception as e:
        print(f'Error: {e}')
        return 'An error occurred', 500

def get_product_price(product_code):
    # fetch product price from database
    pass
