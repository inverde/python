# Define a function to get user input
def get_number(msg):
    while True:
        try:
            n = int(input("Enter a integer as input:? "))

        except ValueError:
            print(msg)
        else:
            return n

def user_number(msg):
     while True:
        try:
            return int(input(msg)) # Pythonic statement

        except ValueError:
            continue    # Pythonic statement

print(user_number("Enter a whole digit:? "))

