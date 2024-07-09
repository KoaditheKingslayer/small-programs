from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print("The current time in UTC is" + now_utc.strftime(format))
# Convert to Asia/Kolkata time zone
now_NY = now_utc.astimezone(timezone('America/New_York'))
print("Your Local Time in America/New_York is " + now_NY.strftime(format))
