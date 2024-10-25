import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.now("US/Eastern")
print(today.month)
delta = today - birth
print(delta.days)

years = delta.days//365
days = delta.days % 365

def days_after_birth(year, month, day):
    """Function to returns the number of days after your birthday"""
    # Define the birth day
    birthday = arrow.get(1961,6,11)
    today = arrow.now("US/Eastern")
    delta = today - birthday
    return delta.days

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

def leap_years_in_age(year_range):
    count = 0
    for year in range(year_range[0], year_range[1]):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            count += 1
    return count

print('Leap days: ', leap_years_in_age((1961, 2024)))

if __name__ == "__main__":
    main()
