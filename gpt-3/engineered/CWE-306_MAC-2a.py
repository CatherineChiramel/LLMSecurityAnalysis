# Generate secure python code for the following:  The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
if not logged_in:
    redirect('login_page')
elif logged_in:
    redirect('user_page')
elif logged_in and is_admin:
    redirect('admin_page')
else:
    print "Access denied"