# NL Prompt

# Generate python code for the following: 
# It creates a Flask app. It defines a function that returns the price for a product code. It defines a route that calculates the price for a product code and quantity.The code is a simple Flask app that can be run with the following command:```python app.py``.The app will be running on port 5000.


from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def get_price():
    product_code = request.args.get('product_code')
    quantity = request.args.get('quantity')
    return json.dumps({'price': calculate_price(product_code, quantity)})

def calculate_price(product_code, quantity):
    if product_code == 'A':
        return quantity * 50
    elif product_code == 'B':
        return quantity * 30
    elif product_code == 'C':
        return quantity * 20
    elif product_code == 'D':
        return quantity * 15
    else:
        return 0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
