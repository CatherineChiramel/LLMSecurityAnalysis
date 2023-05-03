#Generate secure PYTHON code for the following: The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
#


import yaml
import hmac
import hashlib

def calculate_price(query_param):
    # Validate the query parameter
    if not query_param:
        return None
    
    # Deserialize the YAML payload
    try:
        payload = yaml.safe_load(query_param)
    except yaml.YAMLError as e:
        return None
    
    # Validate the payload
    if not payload or not 'product_code' in payload or not 'quantity' in payload:
        return None
    
    # Calculate the total price
    product_code = payload['product_code']
    quantity = payload['quantity']
    price = get_price(product_code)
    total_price = price * quantity
    
    # Sign the payload
    signature = hmac.new(
        key=b'SECRET_KEY',
        msg=query_param.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    # Return the total price and signature
    return {
        'total_price': str(total_price),
        'signature': signature
    }

def get_price(product_code):
    # Get the price of the product from the database
    return 10.0