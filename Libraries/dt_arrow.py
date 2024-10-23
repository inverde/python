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
    regular_days = 23 - 11
    leap_days = 63//4
    print(years, months, regular_days, leap_days)
else:
    print(years, days)

