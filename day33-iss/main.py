from time import sleep

import requests
from datetime import datetime
import smtplib
import time

MY_LATITUDE = 31.200092
MY_LONGITUDE = 29.918739

def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LATITUDE + 5 >= iss_latitude >= MY_LATITUDE - 5 and MY_LONGITUDE + 5 >= iss_longitude >= MY_LONGITUDE - 5:
        return True
    return False

def is_night():
    parameters = {
        "lat" : MY_LATITUDE,
        "lng" : MY_LONGITUDE,
        "formatted" : 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if sunrise >= time_now >= sunset:
        return True
    return False

while True:
    sleep(60)
    if is_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="shiroichii31@gmail.com", password="pkhoyyfiddehxnmi")
            connection.sendmail(from_addr="shiroichii31@gmail.com",
                                to_addrs="shiroichii31@gmail.com",
                                msg="Subject:ISS OVERHEAD!\n\nCheck the ISS overhead now dummy!")