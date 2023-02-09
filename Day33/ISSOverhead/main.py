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

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "date": "02/08/2023"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    local_sunrise = to_local(datetime.fromisoformat(sunrise)).hour
    local_sunset = to_local(datetime.fromisoformat(sunset)).hour
    print(local_sunrise, local_sunset)
    time_now = datetime.now().hour
    if time_now >= local_sunset or time_now <= local_sunrise:
        return True


if is_iss_overhead() and is_night():
    print("ISS is Overhead")
else:
    print("ISS is not overhead")




