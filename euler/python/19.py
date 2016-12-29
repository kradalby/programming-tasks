from datetime import date, timedelta

d1 = date(1901,1,1)
d2000 = date(2000,12,31)
t = timedelta(days=1)

sunday = 0

while d1 != d2000:
    if d1.day == 1 and d1.weekday() == 6:
        sunday += 1
    d1 += t 

print sunday

