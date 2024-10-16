# Floor division executes a division and provide just the whole number as a result without fractional part.
""" Floor division rounds down to an integer the result
This calculation is usuful to convert to system using just whole units like days, hours, minutes and seconds """

# Let's assume we have 1660 minutes and needs to know how many days, hours and minutes are contained

minutes = 1660

hours = minutes // 60


if hours > 24:
    days = hours // 24

hours = hours % 24

minutes = minutes % 60

print(f"There are {days} days, {hours} hours and {minutes} minutes in 1660 minutes")
