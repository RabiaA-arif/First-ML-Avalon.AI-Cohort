# get current time zone in python
import time
import datetime
import pytz
current_time: int = time.localtime()

print(f"current time zone here {current_time}")

print(datetime.__dict__)
# list of all time zone name
# print(pytz.all_timezones)
# tokyo = pytz.country_names
# print(f"Time zone of tokyo: {tokyo}")

# print(pytz.all_timezones)
print(pytz.country_timezones)