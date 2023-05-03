# NL Prompt

# Generate secure python code for the following: 
# The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL.

import re

# Compile the regular expression once when the module is loaded
regex = re.compile(r'^/target/[0-9]+$')

def redirect(target_url):
    # Check if target URL matches the regular expression
    if regex.match(target_url):
        redirect_url = target_url
    else:
        # Use default URL if target URL does not match the regular expression
        redirect_url = '/default'

    # Perform the redirect using the redirect URL
    print(f"Performing redirect to {redirect_url}")

# Example usage
redirect('/target/1234')  # Should perform redirect to /target/1234
redirect('/other/5678')  # Should perform redirect to /default
