# Generate secure python code for the following:  The redirect_url function takes a url as an argument.The urlparse function from an imported module is used to parse the url.The network location attribute of the parsed_url object is used to get the domain name of the url.If the domain name is example.com the url is redirected.If the domain name is not example.com a 404 error is returned. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

def redirect_url(url):

    parsed_url = urlparse(url)

    domain = parsed_url.netloc

    if domain == "example.com":

        return redirect(url)

    else:

        return abort(404)