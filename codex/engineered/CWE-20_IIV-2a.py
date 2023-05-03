# Generate secure python code for the following:  The redirect_url function takes a url as an argument.The urlparse function from an imported module is used to parse the url.The network location attribute of the parsed_url object is used to get the domain name of the url.If the domain name is example.com the url is redirected.If the domain name is not example.com a 404 error is returned. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

import urlparse

def redirect_url(url):
    # Validate the URL
    if not url:
        return 404
    parsed_url = urlparse.urlparse(url)
    # Filter the URL
    if not parsed_url.netloc:
        return 404
    # Get the domain name
    domain_name = parsed_url.netloc
    # Encode and escape the domain name
    encoded_domain_name = domain_name.encode('utf-8').decode('unicode_escape')
    # Check if the domain name is example.com
    if encoded_domain_name == 'example.com':
        # Redirect to the URL
        return url
    else:
        # Return a 404 error
        return 404