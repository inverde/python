# Comparison operator are used in boolean expressions to determine its value

""" Python comparisons operators

>  Greater Than
>= Greater or Equal Than (=> does not work)
<  Less Than
<= Less or Equqal Than (=< does not work)
== Equal Than
!=

"""

# Income assignment
income = 15000

# Conditional statement is one or more connected boolean expressions
low_income = income >= 0 and income < 50000

# Define poverty line levels
poverty_line = income == 15000
above_poverty_line = income >= 15000
below_poverty_line = income <= 15000


print('Variable Type: ', type(low_income))

print('Low income class: ', low_income)

# Conditional Execution (if clause)

# Conditionally print the economic class
if low_income:
    print('Low income class')
    print('Just in the poverty line' )
