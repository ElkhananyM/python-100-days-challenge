import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "OPEN_WEATHER"
MY_LATITUDE = 31.237360
MY_LONGITUDE = 29.994317

weather_parameters = {
    "lat" : MY_LATITUDE,
    "lon" : MY_LONGITUDE,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_condition = response.json()
rain_hours = []

for hour_data in weather_condition["list"]:
    if hour_data["weather"][0]["id"] > 700:
        rain_hours.append(hour_data["dt_txt"].split()[-1].split(":")[0])

if rain_hours:
    account_sid = "acc_sid"
    auth_token = "auth_token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        # from_="+15073575714",
        # body="It's going to rain today, bring an umbrella! ☔️",
        # to="+201115095693"
        from_ = 'whatsapp:+14155238886',
        body=f"It's going to rain today at {", ".join(rain_hours)}, ugh! 🥶🌧️",
        to = 'whatsapp:+20xxxxxxxxxx'
    )
    print(message.status)
