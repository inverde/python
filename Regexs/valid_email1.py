# We need to make sure we @ and .com in our email to make sure is valid
def validate_email():
    """Simple function to see if user input is a email
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
    1. Don't allow less than 8 characters in your username
    2. Allow a period, underscore or hiphen in your username but not all
    3. The username shouldn't start with any special characters or a number
    4. We shouldn't allow more than one @ in the email
    5. The server name may include governmental, commercial, educational and non profit only
    6. The server name may until three compound domain name, or up to 2 dots in the name

"""
if validate_email():
    print("Valid")
else:
    print("Invalid")
