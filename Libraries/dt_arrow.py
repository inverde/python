import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.now("US/Eastern")
print(today.month)
delta = today - birth
print(delta.days)

years = delta.days//365
days = delta.days % 365

if today.month > birth.month:
    months = today.month - birth.month
elif birth.month > today.month:
    months =  12 - (birth.month - today.month)
else:
    months = 0

if today.day > birth.day:
    regular_days = today.day - birth.day
else:
    regular_days = today.ceil('month').date() - (birth.day - today.day)

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

print('Leap years: ', leap_years_in_age((1961, 2024)))
