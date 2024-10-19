# When user fails input ask again
while True:
    try:
        n = int(input("Please enter a number:? "))

    except ValueError:
        print("Value must be a integer")
    else:
        break
print(f"The input entered is {n}")
