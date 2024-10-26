"""
This module works with dates objects to calculate years,months and days
after birthday. This module utilizes the built-in arrow module

Functions:

days_after_birth returns tuple: (days, leap_days)
years_after_birth returns tuple: (years, days)

Calling this module like python dt_arrow.py
"""
import arrow

birth = arrow.get(1961, 6, 11)
print('Type of birthday: ',type(birth))
print(birth.humanize())
today = arrow.now("US/Eastern")
print(today.month)
delta = today - birth
print(delta.days)

years = delta.days//365
days = delta.days % 365

print('Type of years: ', type(years))

def days_after_birth(year, month, day):
    """Function to returns tuple of days and leap_days after birthday
    Inputs:
    year (int) year of birth
    month (int) month of birth
    day (int) day of birth

    Returns:
    tuple: (Days (int), leap_days (int)).
    """
    # Define the birth day
    birthday = arrow.get(1961,6,11)
    today = arrow.now("US/Eastern")
    delta = today - birthday
    leap_days = leap_years_in_age(birthday.year, today.year)
    return delta.days, leap_days

def years_after_birth(days, leap_days):
    """Function to returns tuple with number of years and elapsed extra
    days after birthday
    Inputs:
    days (int) days after birthday
    leap_days (int) leap years after birthday

    Returns:
    tuple: (years (int), days(int))
    """
    return(days // 365, days % 365 - leap_days)

def leap_years_in_age(year_range):
    """Function returns the number leap years occurred during a
    range of years. Consider to adjust this number if were born after february
    and you were born in a leap year.
    Input:
    year_range tuple(birth_year (int), today_year (int)) years range

    Returns:
    int: number of leap years in year range
    """"

    count = 0
    for year in range(year_range[0], year_range[1]):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            count += 1
    return count

def number_months_from_birth(birth_dt, today_dt=arrow.now('US/Eastern'))
if today.month > birth.month:
    months = today.month - birth.month
elif birth.month > today.month:
    months =  12 - (birth.month - today.month)
else:
    months = 0

if today.day > birth.day:
    regular_days = today.day - birth.day
elif birth.day > today.day:
    regular_days = today.ceil('month').date() - (birth.day - today.day)
    months -=1
else:
    regular_days = 0

def main():
    leap_days = leap_years_in_age((birth.year, today.year))
    year_days = years * 365
    month_days = delta.days - year_days - regular_days - leap_days
    print(year_days, month_days, regular_days, leap_days)
    print(years, months, regular_days, leap_days)



print('Leap days: ', leap_years_in_age((1961, 2024)))

if __name__ == "__main__":
    main()
