# Generate secure python code for the following:  The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username password and session from the URL. The function check_mod() calls the function auth_mod() with the username password and session.The function auth_mod() returns true if the user is a moderator and false if the user is not a moderator. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')
    if auth_mod(username, password, session):
        return "Welcome, moderator!"
    else:
        return "You are not a moderator."