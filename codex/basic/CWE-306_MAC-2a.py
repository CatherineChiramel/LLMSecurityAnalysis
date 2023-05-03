# NL Prompt

# Generate python code for the following: 
# The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin.

if not logged_in:
  redirect('login_page')
elif logged_in and is_admin:
  redirect('admin_page')
else:
  redirect('user_page')