# Validating email user input
def validate_email():
    """Simple functin to see if user input is a email
    no arguments() none

    return boolean: True or False
    """
    email = input("What's your email:? ")

    if "@" in email:
        return 
