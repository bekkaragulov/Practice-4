from datetime import datetime, timedelta
#1

print("Date minus 5 days: ", datetime.now - timedelta(days=5))

#2
print("Yesterday ", datetime.now - timedelta(days=1))
print("Today ", datetime.now)
print("Tomorrow ", datetime.now + timedelta(days=1))

#3
now = datetime.now()
micro = now.replace(microsecond=0)
print(micro)

#4

from datetime import datetime

d1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")

print(int(abs((d2 - d1).total_seconds())))