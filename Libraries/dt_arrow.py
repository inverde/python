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
def leap_years_in_age(year_range):
    
if days > 31:
    months = today.month - birth.month
    regular_days = 23 - 11
    leap_days = 63//4
    year_days = years * 365
    month_days = delta.days - year_days - regular_days - leap_days
    print(year_days, month_days, regular_days, leap_days)
    print(years, months, regular_days, leap_days)
else:
    print(years, days)

