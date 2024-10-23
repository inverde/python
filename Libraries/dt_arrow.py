import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.utcnow()
delta = today - birth
print(delta.days)
years = delta.days//365
days = delta.days % 365
if days > 31:
    months = days//30
print(years, days)
year_days = 31+28+31+30+31+30+31+31+30+31+30+31
print(year_days)
