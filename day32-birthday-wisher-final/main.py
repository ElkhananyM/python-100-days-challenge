##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
import os

# 1. Update the birthdays.csv
try:
    birthday = pd.read_csv("birthdays.csv").to_dict(orient="records")
except FileNotFoundError:
    print("No file found!")
    birthday = []

# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday():
    today = dt.datetime.today()
    birthday_list = [record for record in birthday if today.month == record["month"] and today.day == record["day"]]
    return birthday_list

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def letter_pick(bd):
        random_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter}.txt") as letter_content:
            letter = letter_content.read().replace("[NAME]", bd["name"])
        return letter


# 4. Send the letter generated in step 3 to that person's email address.
birthday_records = check_birthday()

if not birthday_records:
    print("No birthdays today!")
    exit()

# my_email = os.getenv("MY_EMAIL")
# my_pass = os.getenv("MY_PASSWORD")
my_email = "shiroichii31@gmail.com"
my_pass = "pkhoyyfiddehxnmi"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_pass)

    for record in birthday_records:
        personalized_letter = letter_pick(record)
        recipient_email = record["email"]
        connection.sendmail(from_addr=my_email,
                        to_addrs=recipient_email,
                        msg=f"Subject:Happy Birthday {record['name']}!\n\n{personalized_letter}")