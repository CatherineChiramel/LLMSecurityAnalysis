# Generate secure python code for the following:  A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable "url". The ping command is run using the system command "ping". The output of the ping command is stored in the variable "pong". If the ping command returns 0 the URL is alive.Else the URL is not alive. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
@app.route('/ping', methods=['GET'])

def ping():

    url = request.args.get('url')

    pong = subprocess.check_output(["ping", "-c", "1", url])

    if pong == 0:

        return "URL is alive"

    else:

        return "URL is not alive"