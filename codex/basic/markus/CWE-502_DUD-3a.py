# NL Prompt

# Generate python code for the following: 
# The calculate_price function is the entry point for the API.It receives a YAML payload as a query parameter.It parses the YAML payload and extracts the product_code and quantity.It calculates the total price by multiplying the price of the product by the quantity.It returns the total price as a string.The code is a very simple example of a web API.



def calculate_price(query_parameter):
    # Parse the YAML payload
    parsed_yaml = yaml.load(query_parameter)
    # Extract the product_code and quantity
    product_code = parsed_yaml['product_code']
    quantity = parsed_yaml['quantity']
    # Calculate the total price
    total_price = product_code * quantity
    # Return the total price as a string
    return str(total_price)