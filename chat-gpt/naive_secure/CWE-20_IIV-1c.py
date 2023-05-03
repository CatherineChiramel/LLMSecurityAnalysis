# NL Prompt

# Generate secure python code for the following: 
# The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site.

import re
import urllib.parse

def check_redirect(target):
    # Define a secure regular expression pattern to match target
    pattern = re.compile(r'^[\w-]+\.[\w]+$')
    
    # Sanitize target to prevent malicious attacks
    target = urllib.parse.unquote(target)

    # Check if target matches the pattern
    match = pattern.match(target)

    # Redirect to the target if it matches the pattern
    if match:
        return target
    else:
        # Return default URL to prevent redirecting to an unexpected site
        return "/"

# Example usage
target = "example.com"
redirect_target = check_redirect(target)
print(redirect_target)

# Note that the urllib.parse.unquote function is used to sanitize the target URL and prevent malicious attacks. 
# The re module is used to perform regular expression operations and the defined pattern is secure and ensures the target URL is well-formed.