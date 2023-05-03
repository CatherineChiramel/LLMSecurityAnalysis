# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message.

def redirect_invalid_url(url):
    if url.startswith("http://example.com"):
        return redirect(url)
    else:
        return "Error: Invalid URL"