def validate_email():
    """Simple function to see if user input is a email
    no arguments() none

    return boolean: True or False
    """
    email = input("What's your email:? ").strip()

    username, domain = email.split('@')

    if username and ".com" in domain:

    if "@" in email and ".com" in email:
        return True
    else:
        return False



def main():
    pass

