import requests
from datetime import datetime
from dateutil import tz

def to_local(time):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    time = time.replace(tzinfo=from_zone)
    local_time = time.astimezone(to_zone)
    return local_time

MY_LAT = 36.7794571 # Your latitude
MY_LONG = -76.5355366 # Your longitude

response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
response.raise_for_status()
data = response.json()

print(data)

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

local_sunrise = to_local(datetime.fromisoformat(sunrise))
local_sunset = to_local(datetime.fromisoformat(sunset))


print(local_sunrise.hour, local_sunset.hour)



