# Shows an example on how to handle exception
try:
    n = int(input("Please enter a number:? "))

except ValueError:
    print(f"Your input must be a integer")

else:
    print(f"The value of your input is {x}")

