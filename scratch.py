import datetime
import time
import calendar

epoch=1617236100

mytimestamp = datetime.datetime.fromtimestamp( epoch )
datetime_str = mytimestamp.strftime("%Y-%m-%d %H:%M:%S")
print("Converted datetime string:", datetime_str)

print(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(epoch)))

print(calendar.timegm(time.strptime('01-04-2021', '%d-%m-%Y')))
print(calendar.timegm(time.strptime('23-03-2021 00:00:00', '%d-%m-%Y %H:%M:%S')))

print(calendar.timegm(time.strptime('23-03-2021 00:00:00', '%d-%m-%Y %H:%M:%S'))-calendar.timegm(time.strptime('22-03-2021', '%d-%m-%Y')))
print(24*60*60)

regex = '\d{2}-\d{2}-\d{4}'
