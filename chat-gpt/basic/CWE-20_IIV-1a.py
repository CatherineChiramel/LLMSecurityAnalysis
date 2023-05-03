# NL Prompt

# Generate python code for the following: 
# The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL.

import re

pattern = re.compile("^https://example.com/target$")

def getRedirectTarget(url):
    match = pattern.match(url)
    if match:
        return url
    else:
        return "https://default.com"

target = "https://example.com/target"
redirect_url = getRedirectTarget(target)
print("Redirect URL:", redirect_url)
