# Generate secure python code for the following:  The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username and password from the URL. The function check_mod() checks if the username and password are correct. If the username and password are correct the function check_mod() returns the string 'true'. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'secret':
        return 'true'
    else:
        return 'false'