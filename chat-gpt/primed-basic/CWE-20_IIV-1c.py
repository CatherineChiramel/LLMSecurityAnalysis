# NL Prompt

# "Generate python code for the following The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site."

from flask import Flask, redirect, abort, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect_url', methods=['GET'])
def redirect_url():
    url = request.args.get('url')

    if url:
        parsed_url = urlparse(url)

        if parsed_url.netloc == 'example.com':
            return redirect(url)
        else:
            abort(404)

    abort(400)

if __name__ == '__main__':
    app.run(debug=True)
