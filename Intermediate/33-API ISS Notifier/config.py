import requests
import pytz
from datetime import datetime

MY_LAT = 12.9716
MY_LONG = 77.5946

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()



print("Sunrise:", sunrise_ist.strftime("%H:%M"))
print("Sunset:", sunset_ist.strftime("%H:%M"))
