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
    no arguments() none

    return boolean: True or False
    """

    email = input("What's your email:? ").strip()


    if re.search(r"^(\w{8,15}-?_?)(\w+\.?)@(.+)\.(com|edu|org|gob|gov)$",
                email, re.IGNORECASE):
        return True
    else:
        return False

if validate_email():
    print("Valid email")
else:
    print("Invalid email")
