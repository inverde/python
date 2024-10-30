# Validating email with regex
import re
def validate_email():

    formatUser = r"^[^\W\d\s_]([a-zA-Z0-9]\.?-?_?){8,20}"

    formatDomain = r"^[^@](\w+\.+)\.(com|edu|gov|gob|org)$"

    email = input("What's your email:? ").rstrip()

    username, domain = email.split('@')

    print(username, domain)

    if re.search(formatUser, username) and re.search(formatDomain, domain):
        return True
    else:
        return False

if validate_email():
    print("Valid")
else:
    print("Invalid")

