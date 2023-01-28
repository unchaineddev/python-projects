STOCK_NAME = "GOOGL"
COMPANY_NAME = "Google LLC"

STOCK_API ="0Y9JB9BQNPF19805"
NEWS_API = "99be5b84014d45259709f1c1a79708d2"


MY_EMAIL = "----email----"
MY_PASS = "----passsword----"

import requests
import smtplib


stock_param = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": "GOOGL",
        "apikey": STOCK_API
        }


news_param = {
        "q": "GOOGL",
        "apikey": NEWS_API
        }

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


response = requests.get(url=STOCK_ENDPOINT, params=stock_param)
# print(response.status_code)
data = response.json()


daily_stock_data = response.json()["Time Series (Daily)"]

# Convert Dict to list 
data_list = [value for (key,value) in daily_stock_data.items()]

# Yesterday close price
yesterday_price = data_list[0]
yesterday_closing = yesterday_price["4. close"]
#print(yesterday_closing)

# Get the day before yesterday's closing stock price
day_before_yest_price = data_list[1]
day_before_yest_close = day_before_yest_price["4. close"]
#print(day_before_yest_close)

# Find the positive difference

difference_in_price = abs(float(yesterday_closing) - float(day_before_yest_close))
#print(difference_in_price)


# Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.

perc_diff = difference_in_price/float(day_before_yest_close) * 100
#print(perc_diff)

# If percentage is greater than 5 then print("Get News").

if perc_diff>1:
    #print("Get News")
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    print(news_response.status_code)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_article = [f"Headline: {article['title']} \n Brief:{article['description']}" for article in three_articles]

    with smtplib.SMTP(host="smtp.gmail.com") as new_connection:
        new_connection.starttls()
        new_connection.login(user=MY_EMAIL,password=MY_PASS)
        new_connection.sendmail(from_addr=MY_EMAIL, to_addrs="--email--",msg=f"Subject: Hello Googl \n\n {formatted_article}")
