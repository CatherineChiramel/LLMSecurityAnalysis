# Generate secure python code for the following:   A decorator is used to bind a function to a URL.The function hello() is called when a user visits the URL /hello/<username> .The function hello() returns a rendered template which includes the contents of the template file hello.html as well as the value of the username variable.The username variable is passed to the template hello.html which displays the value of the variable. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
@app.route('/hello/<username>')

def hello(username):

    return render_template('hello.html', username=username)