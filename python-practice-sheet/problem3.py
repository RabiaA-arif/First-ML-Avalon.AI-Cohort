# get current time zone in python
import time
from datetime import datetime
import pytz
from zoneinfo import ZoneInfo
current_time: int = time.localtime()

# print(f"current time zone here {current_time}")

# print(datetime.__dict__)
# list of all time zone name
print(pytz.all_timezones)
# tokyo = pytz.country_names
# print(f"Time zone of tokyo: {tokyo}")

# print(pytz.all_timezones)
# print(pytz.country_timezones)

# print(ZoneInfo.tzname())




print("Time zone of Pakistan")
pkr = ZoneInfo("Asia/Karachi")
tim = datetime.now(pkr)
print(tim)
print("\n")

print("Time zone of new york")
tz = ZoneInfo("America/New_York")
dt = datetime.now(tz)
print(dt)
print("\n")


print("Time zone of tokyo")
tzz = ZoneInfo("Asia/Tokyo")
dtt = datetime.now(tzz)
print(dtt)
print("\n")

print("Time zone of Turkey")
turk = ZoneInfo('Turkey')
ttm = datetime.now(turk)
print(ttm)
