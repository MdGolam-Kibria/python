import time
from datetime import datetime

currentDate = datetime.now()
print(currentDate)

currentDay = datetime.now().day
print(currentDay)

print(datetime.now().minute)  # current minute
print(datetime.now().second)  # current second
print(datetime.now().time())  # current time
# for get timeStamp
timestamp = int(time.time())
print(timestamp)
