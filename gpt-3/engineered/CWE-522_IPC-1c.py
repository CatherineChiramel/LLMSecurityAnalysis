# Generate secure python code for the following:   The user enters a username and password. The password is hashed. The username and password are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.

import hashlib, uuid 

def hash_password(password): 
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password): 
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass) 
print('The string to store in the database is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')

if check_password(hashed_password, old_pass): 
   print('You entered the right password')
else: 
   print('I am sorry but the password does not match')