import smtplib
import datetime as dt
import random
my_email = "dhdfghfhdg@gmail.com"
password = "dhfhdhdfgh"

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def send_email():
    # Create a new SMTP object connection
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # call TLS (Transport Layer Security) to secure the connection to the email server
        connection.starttls()

        # login to the email server
        connection.login(user=my_email, password=password)
        # send email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="visionaijaz@gmail.com",
            msg= f"Subject:{day[day_of_week]} Motivational Quote\n\n{message}"
        )

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week ==3:
    # read quotes.txt file
    with open("quotes.txt") as file:
        quotes = file.readlines()
        message = quotes[random.randint(0, len(quotes) - 1)]
    send_email()