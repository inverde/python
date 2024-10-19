# Define a function to get user input
def get_number(msg): # msg for exception error
    while True:
        try:
            n = int(input("Enter a integer as input:? "))

        except ValueError:
            print(msg)
        else:
            return n

def user_number(msg): # msg asking user for input
     while True:
        try:
            return int(input(msg)) # Pythonic statement

        except ValueError:
            continue    # Pythonic statement

if __name__ == "__main__":
    print(user_number("Enter a whole digit:? "))

