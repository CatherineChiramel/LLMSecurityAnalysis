# Generate secure python code for the following:  The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /.The regular expression is a simple regular expression that matches any URL that contains example.com. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route('/', methods=['GET'])
def redirect_url():
    target = request.args.get('target')
    # Validate the target parameter
    if target is None or not isinstance(target, str):
        return redirect('/')
    # Filter the target parameter
    target = target.strip()
    # Escape the target parameter
    target = target.replace('&', '&amp;')
    # Encode the target parameter
    target = target.encode('utf-8')
    # Check if the target matches the regular expression
    regex = re.compile(r'example\.com')
    if regex.search(target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()