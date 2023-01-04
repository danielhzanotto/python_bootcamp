import datetime as dt

now = dt.datetime.now()

print(now)
year = now.year
print(year)

weekday = now.weekday()
print(weekday)


date_of_birth = dt.datetime(year=1994, month=2, day=1, hour=6, minute=14)
print(date_of_birth)
