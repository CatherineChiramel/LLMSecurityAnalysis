# NL Prompt

# "Generate python code for the following It creates a Flask app. It defines a function that returns the price for a product code. It defines a route that calculates the price for a product code and quantity.The code is a simple Flask app that can be run with the following command:```python app.py``.The app will be running on port 5000."

from flask import Flask, request

app = Flask(__name__)

# Define a function to return the price for a product code
def get_price(product_code):
    # This is just a placeholder implementation
    prices = {"A001": 100, "B002": 200, "C003": 300}
    return prices.get(product_code, None)

# Define a route that calculates the price for a given product code and quantity
@app.route('/calculate_price')
def calculate_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity', 1))
    price = get_price(product_code)
    if price is None:
        return f"Product code {product_code} not found"
    total_price = price * quantity
    return f"Total price for {quantity} units of {product_code} is {total_price}"

if __name__ == '__main__':
    app.run(port=5000)
