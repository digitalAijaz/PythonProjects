import requests
from datetime import datetime
import time
import pytz

MY_LAT = 12.9716
MY_LONG = 77.5946

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_utc = datetime.strptime(data["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
sunset_utc = datetime.strptime(data["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z")

bangalore_timezone = pytz.timezone("Asia/Kolkata")
time_now = datetime.now(bangalore_timezone)

def is_iss_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False

def is_dark():
    if time_now >= sunrise_utc.astimezone(bangalore_timezone) and time_now <= sunset_utc.astimezone(bangalore_timezone):
        return False
    else:
        return True

def send_email():

    import smtplib

    my_email = "totekhan90@gmail.com"
    password = "ggrqmptodiuagwrr"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="visionaijaz@gmail.com",
            msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
        )

#If the ISS is close to my current position # and it is currently dark
# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    time_now = datetime.now(bangalore_timezone)
    if is_iss_overhead() and is_dark():
        send_email()
    else:
        print("ISS is out of reach.")




