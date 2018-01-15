import datetime
now = datetime.datetime.now()
yesterday = datetime.datetime(2017, 1, 14, 19, 30)
print(yesterday)
delta = now - yesterday
print(delta.days)
print(delta.total_seconds())
strnow = now.strftime("%Y%m%d%B")
#strftime.org
print(strnow)

after=now+datetime.timedelta(days=2)
print(after)
