import arrow
birth = arrow.get(1961, 6, 11)
print(birth.humanize())
today = arrow.utcnow()
delta = today - birth
print(delta.years)

