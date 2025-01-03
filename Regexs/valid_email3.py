# Using the built-in library re make sure we use regular expressions to validate email

""" Regular Expressions:
    .   any character except a new line
    *   0 or more repetitions
    +   1 or more repetitions
    ?   0 or 1 repetition
    {m} m repetitions
    {m,n} m-n repetitions
"""
def validate_email():
    """Simple function to see if user input is a email
    no arguments() none

    return boolean: True or False
    """

    email = input("What's your email:? ").strip()

    username, domain = email.split('@')

    if username and domain.endswith('.edu'):
        return True
    else:
        return False

if validate_email():
    print("Valid email")
else:
    print("Invalid email")
