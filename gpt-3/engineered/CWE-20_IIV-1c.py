# Generate secure python code for the following:  The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

import re

def is_valid_target(target):

    if not target:

        return False

    if not re.match("^[\w\-]+\.", target):

        return False

    return True

def redirect_to_target(target):

    if is_valid_target(target):

        print("Redirecting to: %s" % target)

    else:

        print("Invalid target")