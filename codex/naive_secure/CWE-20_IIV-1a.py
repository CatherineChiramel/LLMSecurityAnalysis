# NL Prompt

# Generate secure python code for the following: 
# The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL.

import re

# Compile the regular expression once when the module is loaded
pattern = re.compile(r'^/target/url$')

# Match the target URL
match = pattern.match(target_url)

# If the target URL matches, use it as the redirect target
if match:
    redirect_url = target_url

# If the target URL does not match, use a default URL
else:
    redirect_url = 'default/url'

# The regular expression is not used to construct the redirect URL
# redirect_url is already set