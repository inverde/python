# Validate the use of up to one dot in the username
import re
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
    This function allows one dot in the user name and up
    to 15 characters but not less than eight.

    arguments(): none

    return boolean: True or False
    """

    email = input("What's your email:? ").strip()


    if re.search(r"^[a-zA-Z0-9][a-zA-Z]\.?{8,15}@(.+)\.(com|edu|org|gob|gov)$",
                email, re.IGNORECASE):
        return True
    else:
        return False

if validate_email():
    print("Valid email")
else:
    print("Invalid email")
