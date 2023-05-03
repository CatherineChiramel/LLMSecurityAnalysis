# Generate secure python code for the following:  A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import os
from functools import wraps

def secure_img(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        name = kwargs.get('name')
        if name:
            name = os.path.normpath(name) # get canonical version of file path
            name = os.path.basename(name) # get only the file name, not the path
            if not name.startswith('img'): # input validation
                raise Exception("Invalid file name")
        return f(*args, **kwargs)
    return decorated_function

@secure_img
def img(name):
    with open(os.path.join('images', name), 'rb') as f:
        return f.read()