import datetime
import time
import random

time_interval = random.randint(115200, 151200)
print(time_interval)

a = datetime.time(12,20,59,899)
a.__format__('%H:%M:%S')

a = datetime.time(12,20,59,899)
a.strftime('%H:%M:%S')
'12:20:59'

#合并日期和时间
datetime.datetime.combine(a.date(),a.time())
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)

timestr = '2015-07-30 00:00:00'
timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
sign_timeArray = timeStamp + time_interval
print(sign_timeArray)
timeArray = time.localtime(sign_timeArray)
sign_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(sign_time)

print("hello")
