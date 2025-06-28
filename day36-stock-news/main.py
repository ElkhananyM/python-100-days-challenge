import requests
from itertools import islice
import pandas as pd
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_API_KEY = "ALPHA_KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = "NEWS_KEY"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHA_VANTAGE_API_KEY
}

# response = requests.get(ALPHA_VANTAGE_ENDPOINT, stock_parameters)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]
# data = dict(islice(stock_data.items(), 2))
stock_data = pd.read_csv("daily_IBM.csv")
data = stock_data.to_dict(orient="records")[:2]
# print(stock_data)
# print(data)

prices = []
for day in data:
    prices.append(day["close"])
if abs(prices[0] - prices[1]) / prices[0] * 100 < 5:
    print(prices)
    print("Get news!")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    "apiKey" : NEWS_API_KEY,
    "country" : "us",
    "q" : "intel",
}

response = requests.get(NEWS_ENDPOINT, news_parameters)
response.raise_for_status()
news_response = response.json()
# print(type(news_response))
# print(news_response["articles"][0]["title"])
direction = "🔺" if prices[0] > prices[1] else "🔻"
change_rate = (abs(prices[0] - prices[1]) / prices[0]) * 100
for article in news_response["articles"][:3]:
    print(f"{STOCK}: {direction} {change_rate:0.2f}%\nHeadline: {article["title"]}.\nBrief: {article["description"]}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# account_sid = ''
# auth_token = ''
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#   from_="whatsapp:+14155238886",
#   content_sid="",
#   body=f"",
#   to="whatsapp:+20xxxxxxxxxx"
# )

# print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""

