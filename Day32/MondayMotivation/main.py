#import smtplib
#
#my_email = "herseyc@gmail.com"
#my_password = ""
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#connection.starttls()
#connection.login(user=my_email, password=my_password)
#connection.sendmail(from_addr=my_email,
#                    to_addrs="hcartwright@vmware.com",
#                    msg="Subject: Hello\n\nThis is the email.")

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day = now.month
day_of_week = now.weekday()
print(now)
print(day_of_week)

date_of_birth = dt.datetime(year=1972, month=7, day=31)
print(date_of_birth)

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    quote = random.choice(quote_list)

# Print Quote if day of week is Monday
if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        quote = random.choice(quotes_list)
    print(quote)

#Not doing any SMTP here... since I am not saving the password.