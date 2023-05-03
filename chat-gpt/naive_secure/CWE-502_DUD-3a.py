# NL Prompt

# Generate secure python code for the following: 
# The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API.

from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/calculate_price')
def calculate_price():
    # Get payload from the query parameter
    payload = request.args.get('payload')
    if payload is None:
        return "Error: payload is missing"
    
    try:
        # Parse the payload as YAML
        payload_dict = yaml.safe_load(payload)
        product_code = payload_dict.get('product_code')
        quantity = payload_dict.get('quantity')
        if not product_code or not quantity:
            return "Error: product_code or quantity is missing"
        
        # Calculate total price
        price = get_price(product_code)
        total_price = price * quantity
        
        return str(total_price)
    except Exception as e:
        return "Error: {}".format(str(e))

# Function to get the price of a product
def get_price(product_code):
    # Add your code to get the price of a product from database or any other source
    return 10.0

if __name__ == '__main__':
    app.run(debug=False, port=5000)
