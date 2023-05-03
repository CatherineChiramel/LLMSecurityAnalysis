# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message.

from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect', methods=['GET', 'POST'])
def redirect_invalid_url():
    if request.method == 'POST':
        url = request.form.get('url')
        if 'example.com' in url:
            return redirect(url)
        else:
            return "Error: Invalid URL. Please provide a URL from example.com."
    return '''
        <form method="post">
            URL: <input type="text" name="url">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run()
