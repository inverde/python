from conditional_execution import conditional_execution
# Floor division executes a division and provide just the whole number as a result without fractional part.
""" Floor division rounds down to an integer the result
This calculation is usuful to convert to system using just whole units like days, hours, minutes and seconds """

# Let's assume we have 1660 minutes and needs to know how many days, hours and minutes are contained

minutes = 1660

# Conversion function using the modulus function: return the fractional part of the floor function
def minutes_to_days(minutes):
    hours = minutes // 60
    if hours > 24:
        days = hours // 24
        hours = hours % 24
    else:
        days = 0
    minutes = minutes % 60
    return days, hours, minutes

days, hours, minutes = minutes_to_days(minutes)

print(f"There are {days} days, {hours} hours and {minutes} minutes in 1660 minutes")

days, hours, minutes = conditional_execution(1660, True, minutes_to_days)

print('Days, hours, minutes:', days, hours, minutes)

