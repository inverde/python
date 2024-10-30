# We need to make sure we @ and .com in our email to make sure is valid
def validate_email():
    """Simple functin to see if user input is a email
    no arguments() none

    return boolean: True or False
    """
    email = input("What's your email:? ")

    if "@" in email and ".com" in email:
        return True
    else:
        return False
""" How many other rules we need to add for a valid a email
    Add at least three of them:
    1.
    2.
    3.
"""
if validate_email():
    print("Valid")
else:
    print("Invalid")
