# Shows an example on how to handle exception
try:
    n = int(input("Please enter a number:? "))

except ValueError:
    print(f"Your input is {n}")

