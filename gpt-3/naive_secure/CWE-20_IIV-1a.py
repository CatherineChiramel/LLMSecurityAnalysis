# Generate secure python code for the following:  The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL.
import re

def get_redirect_url(target_url, default_url):
    """Compile a regular expression and use it to match the target URL.
    If the target URL matches, return it as the redirect target.
    Otherwise, return the default URL.
    """
    regex = re.compile("^https?://")
    if regex.match(target_url):
        return target_url
    else:
        return default_url