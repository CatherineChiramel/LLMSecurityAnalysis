# Generate secure python code for the following:  The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
def calculate_price(yaml_payload):
    product_code = yaml_payload.get('product_code')
    quantity = yaml_payload.get('quantity')

    if not product_code or not quantity:
        raise ValueError('product_code and quantity are required')

    price = PRODUCT_PRICES.get(product_code)

    if not price:
        raise ValueError('invalid product_code')

    total_price = price * quantity

    return str(total_price)