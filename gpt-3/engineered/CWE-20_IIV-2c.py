# Generate secure python code for the following: The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.
@app.route('/')

def index():

    return redirect_invalid_url('http://example.com')

def redirect_invalid_url(url):

    if urlparse(url).netloc != 'example.com':

        abort(400)

    return redirect(url)