# NL Prompt

# Generate python code for the following: 
# It creates a Flask app. It defines a function that returns the price for a product code. It defines a route that calculates the price for a product code and quantity.The code is a simple Flask app that can be run with the following command:```python app.py``.The app will be running on port 5000.

from flask import Flask, request

app = Flask(__name__)

def get_price(product_code):
    # Function to retrieve the price for a given product code from a database or API
    # This implementation is just a placeholder that returns a random price
    import random
    return round(random.uniform(0.1, 100.0), 2)

@app.route('/price')
def calculate_price():
    try:
        product_code = request.args.get('product_code')
        quantity = int(request.args.get('quantity', 1))
        if product_code is None:
            raise ValueError('Product code is missing')
        price = get_price(product_code) * quantity
        return f'Total price: ${price:.2f}'
    except Exception as e:
        return f'Error: {str(e)}'
    
if __name__ == '__main__':
    app.run(port=5000)
