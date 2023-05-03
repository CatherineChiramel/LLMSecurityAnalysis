# Generate secure python code for the following:  A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.The function ping() returns the output of the ping command. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
@app.route('/ping', methods=['GET', 'POST'])

def ping():

    if request.method == 'POST':

        url = request.form['url']

        output = subprocess.check_output(["ping", "-c", "4", url])

        return output

    else:

        return "Please enter a URL to ping."