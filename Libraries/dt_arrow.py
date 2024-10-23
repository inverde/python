import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.utcnow()
delta = today - birth
print(delta.days)
years = delta.days//365
days = delta.days % 365
if days > 31:
    months = 
    days = days % 31
    print(years, months, days)
else:
    print(years, days)

