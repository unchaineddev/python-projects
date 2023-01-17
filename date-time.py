import datetime as dt

now = dt.datetime.now()
#now = datetime.datetime.now()
print(now)

year = now.year
print(year)


month = now.month
print(month)

week = now.weekday()
print(week)


dob = dt.datetime(year=2000, month=6, day=27)
print(dob)
