"""
This module works with dates objects to calculate years,months and days
after birthday. This module utilizes the built-in arrow module

Functions:

days_after_birth(year, month, day) returns tuple: (days, leap_days) days, leap_days in days
years_from_birth(days, leap_days) returns tuple: (years, days) years and extra days
leap_years_in_age((birth_year, today_year)) returns int: leap_days
months_from_birth(birth_dt, today_dt) returns int: months in age
days_from_birth(birth_dt, today_dt) returns int: days in age

Calling this module like python dt_arrow.py
"""
import arrow


def days_after_birth(year, month, day):
    """Function to returns tuple of days and leap_days after birthday
    Inputs:
    year (int) year of birth
    month (int) month of birth
    day (int) day of birth

    Returns:
    tuple: (days_alive (int), leap_days (int)).
    """
    # Define the birth day
    birthday = arrow.get(year, month, day)
    today = arrow.now("US/Eastern")
    delta = today - birthday
    leap_days = leap_years_in_age(birthday.year, today.year)
    return delta.days, leap_days

def years_from_birth(days, leap_days):
    """Function to returns tuple with number of years and elapsed extra days
    excluding leap days in years
    Inputs:
    days (int) days alive after birthday
    leap_days (int) leap days after birthday

    Returns:
    tuple: (years (int), days(int))
    """
    return(days // 365, days % 365 - leap_days)

def leap_years_in_age(year_range):
    """Function returns the number leap years occurred during a
    range of years. Consider to adjust this number if you were born after february
    and during a leap year.
    Input:
    year_range tuple(birth_year (int), today_year (int)) years range

    Returns:
    int: number of leap years in year range
    """

    count = 0
    for year in range(year_range[0], year_range[1]):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            count += 1
    return count

def months_from_birth(birth_dt, today_dt=arrow.now('US/Eastern')):
    """Function to returns the number of months since your birthday
    Inputs:
    birth_dt (arrow object) Date of your birthday
    today_dy (arrow object) Today's date

    Returns:
    int: Number of months elapsed since your birthday
    """

    if today_dt.month > birth_dt.month:
        months = today_dt.month - birth_dt.month
    elif birth_dt.month > today_dt.month:
        months =  12 - (birth_dt.month - today_dt.month)
    else:
        months = 0

    return months

def days_from_birth(birth_dt, today_dt=arrow.now('US/Eastern')):
    """Function to return the number of days other than years and months lived
    since your birthday
    Inputs:
    birth_dt (arrow object) Date of your birthday
    today_dt (arrow object) Today's date

    Returns:
    int: Number of days in addition of years and months since birthday
    """

    if today_dt.day > birth_dt.day:
        regular_days = today_dt.day - birth_dt.day
    elif birth_dt.day > today_dt.day:
        regular_days = today_dt.ceil('month').date() - (birth_dt.day - today_dt.day)
        months -=1
    else:
        regular_days = 0

    return regular_days

def main():
    """Function to print years in days, months in days, regular days, leap days,
    and also print years, months, regular days and leap years since birthday
    """
    birth = arrow.get(1961, 6, 11)
    today = arrow.now("US/Eastern")
    delta = today - birth

    years = delta.days//365
    months = months_from_birth(birth, today)
    days = delta.days % 365

    leap_days = leap_years_in_age((birth.year, today.year))
    year_days = years * 365
    regular_days = days_from_birth(birth, today)
    month_days = delta.days - year_days - regular_days - leap_days

    print(year_days, month_days, regular_days, leap_days)
    print(years, months, regular_days, leap_days)


if __name__ == "__main__":
    main()
