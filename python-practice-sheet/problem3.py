# get current time zone in python
import time
import datetime
import pytz
from zoneinfo import ZoneInfo
current_time: int = time.localtime()

# print(f"current time zone here {current_time}")

# print(datetime.__dict__)
# list of all time zone name
# print(pytz.all_timezones)
# tokyo = pytz.country_names
# print(f"Time zone of tokyo: {tokyo}")

# print(pytz.all_timezones)
# print(pytz.country_timezones)



# print(ZoneInfo.tzname())


# pkr = ZoneInfo("Asia/Pakistan")
# tim = datetime.now(pkr)
# print(tim)


from datetime import datetime
from zoneinfo import ZoneInfo

# Get current time in a specific timezone
tz = ZoneInfo("America/New_York")
dt = datetime.now(tz)
print(dt)
# Get the offset name (e.g., EST, EDT) and time difference
tz_name = dt.tzname()
utc_offset = dt.utcoffset()

print(f"Timezone: {tz_name}")
print(f"Difference from UTC: {utc_offset}")
# Output: Difference from UTC: -5:00:00 (or -4:00:00 during Daylight Saving Time)


tzz = ZoneInfo("Asia/Tokyo")
dtt = datetime.now(tzz)
print(dtt)