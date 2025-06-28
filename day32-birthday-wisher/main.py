# import smtplib
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# my_email = os.getenv("EMAIL_ADDRESS")
# password = os.getenv("EMAIL_PASSWORD")
# print(my_email, password)
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="shiroichiitesting@gmail.com",
#                         msg="Subject:Hello\n\nKonnichihwa body 5"
#                         )


import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import random

now = dt.datetime.now()
day_of_week = now.weekday()

try:
    with open(file="quotes.txt", mode="r") as data:
        quotes = data.readlines()
except:
    print("File not Found!")
if day_of_week == 5:
    load_dotenv()
    my_email = os.getenv("EMAIL_ADDRESS")
    my_password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="shiroichiitesting@gmail.com",
                            msg=f"Subject:Motivational Quote of The Week!\n\n{random.choice(quotes)}")