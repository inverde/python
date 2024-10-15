# Comparison operator are used in boolean expressions to determine its value

# Equal comparison
income = 15000

# Conditional statement
low_income = income >= 0 and income < 50000

print(type(low_income))

print(low_income)

# Conditional Execution (if clause)

# Conditionally print the economic class
if low_income:
    print('Low income class')
