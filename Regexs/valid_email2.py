# Validating email with regex
import re
def validate_email():

    formatUser = r"^[^\W\d\s_]([a-zA-Z0-9]\.?-?_?){8,20}"

    # formatDomain = r"^(^@\w\.?)\.(com|edu|gov|gob|org]$"

    email = input("What's your email:? ").strip()

    username, domain = email.split('@')

    print(username, domain)

    if re.search(formatUser, username):
        return True
    else:
        return False

if validate_email():
    print("Valid")
else:
    print("Invalid")

