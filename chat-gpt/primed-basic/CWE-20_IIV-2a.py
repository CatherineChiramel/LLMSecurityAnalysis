# NL Prompt

# "Generate python code for the following The redirect_url function takes a url as an argument.The urlparse function from an imported module is used to parse the url.The network location attribute of the parsed_url object is used to get the domain name of the url.If the domain name is example.com the url is redirected.If the domain name is not example.com a 404 error is returned."

from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    if 'example.com' in url:
        return redirect(url)
    else:
        return abort(400)

if __name__ == '__main__':
    app.run(debug=True)
