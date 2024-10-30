# Validating email with regex
import re
def validate_email():
    """ Function to validate email with regular expressions following these rules:
    1. Don't allow less than 8 characters in your username
    2. Allow a period, underscore or hiphen in your username but not all
    3. The username shouldn't start with any special characters or a number
    4. We shouldn't allow more than one @ in the email
    5. The server name may include governmental, commercial, educational and non profit only
    6. The server name may until three compound domain name, or up to 2 dots in the name

    no arguments() none

    return boolean: True or False

    Validating two groups of characters: username and servername
    username:^[^\W\s\d][\w][\.|-|_]?{8,20}
    servername: [^@][\w][_-\.]?[.com|.edu|.gov|.gob|.org]$

    """
    formatUser = r"^[^\W\s\d][\w][\.|-|_]?{8,20}"
    formatDomain = r"[^@][\w][_-\.]?[.com|.edu|.gov|.gob|.org]$"

    email = input("What's your email:? ").strip()

    username, domain = email.split('@')

    if re.search(formatUser, username) and re.search(formatDomain, domain):
        return True
    else:
        return False

if validate_email():
    print("Valid")
else:
    print("Invalid")

