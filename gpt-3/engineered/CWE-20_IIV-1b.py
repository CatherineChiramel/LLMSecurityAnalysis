# Generate secure python code for the following:  The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /.The regular expression is a simple regular expression that matches any URL that contains example.com. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.
import re

from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')

def index():

    target = request.args.get('target')

    if target is None:

        return redirect('/')

    if not re.match(r'^https?://(www\.)?example\.com', target):

        return redirect('/')

    return redirect(target)