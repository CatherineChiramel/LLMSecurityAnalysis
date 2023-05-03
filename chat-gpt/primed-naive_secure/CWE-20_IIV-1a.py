# NL Prompt

# "Generate secure python code for the following The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL."

import re

# Compile the regular expression pattern once when the module is loaded
url_pattern = re.compile(r'https?://example.com/path/.*')

def redirect_url(target_url):
    # Check if the target URL matches the regular expression pattern
    if url_pattern.match(target_url):
        # Use the target URL as the redirect target
        redirect_url = target_url
    else:
        # Use the default URL as the redirect target
        redirect_url = 'https://example.com/default/path'
    return redirect_url
