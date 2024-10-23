import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.now("US/Eastern")
print(today.month)
delta = today - birth
print(delta.days)
years = delta.days//365
days = delta.days % 365
if days > 31:
    months = today.month - birth.month
    regular_days = (31-23) + 11
    leap_days = delta.days - (years * 365) - (months * 30) - regular_days
    print(years, months, regular_days, leap_days)
else:
    print(years, days)

