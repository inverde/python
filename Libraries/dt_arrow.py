import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.now("US/Atlantic")
print(today)
delta = today - birth
print(delta.days)
years = delta.days//365
days = delta.days % 365
if days > 31:
    months = days//31
    days = days % 31
    print(years, months, days)
else:
    print(years, days)

