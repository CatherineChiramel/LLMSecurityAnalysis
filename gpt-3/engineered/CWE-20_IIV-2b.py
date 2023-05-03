# Generate secure python code for the following:  The code is a simple web application that has a route /redirect/<url> that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL is from example.com. If it is it redirects the user to the URL. If it is not it returns an error message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
    if not url.startswith('http://example.com'):
        return render_template('error.html', message='Invalid URL')
    return redirect(url)