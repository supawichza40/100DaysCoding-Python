from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
load_dotenv()

def get_stock_price_from_portfolio_list():
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    result = response.json()["Time Series (Daily)"]  # Get only daily data without metadata.
    return result

def get_date_and_closing_price_only() -> dict:
    new_dict = {key: value["4. close"] for key, value in
                dict(result).items()}  # create a new dict with only close price and date
    return new_dict
# add the news to top 3 news to send to sms.
def add_top3_news_from_news_api():
    if len(news_data) > 3:
        for index in range(3):
            top3_news.append(news_data[index])
    else:
        for index in range(len(news_data)):
            top3_news.append(news_data[index])


def get_news_api_data():
    new_response = requests.get(url=NEWS_END_POINT, params=news_api_param)

    news_data = new_response.json()["articles"]
    return news_data


def send_top3_news_to_mobile():
    if percentage_difference > 0:
        price_increase_or_decrease = f"TSLA: 🔺{round(percentage_difference, 2)}%"
    else:
        price_increase_or_decrease = f"TSLA: 🔻{round(percentage_difference, 2)}%"
    for new in top3_news:
        message = client.messages.create(
            body=f'{price_increase_or_decrease}\n\nHeadline:{new["title"]}\nBrief:{new["description"]}\nURL:{new["url"]}',
            from_=TWILIO_NUMBER,
            to='+447377515606'
        )

        print(message.sid)

def convert_datekey_to_indexkey() -> dict:
    counter = 0
    new_dict2 = {}
    # convert dictionary from date key into index key, for easier access.
    for key, value in date_closing_price_dict.items():
        new_dict2[counter] = {
            "date": key,
            "price": float(value)
        }
        counter += 1
    return new_dict2


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = "ACef08d2c54acc66333a64d92dfec4fb87"
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_NUMBER = "+15632782109"
NEWS_END_POINT = "https://newsapi.org/v2/everything"
top3_news = []
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API_KEY
}

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)
price_increase_or_decrease = ""


result = get_stock_price_from_portfolio_list()
date_closing_price_dict = get_date_and_closing_price_only()
index_key_stock = convert_datekey_to_indexkey()
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_param = {
    "apiKey": NEWS_API_KEY,
    "q": "tesla",
    "searchIn": "title",
    "from": index_key_stock[1]["date"],
    "to": index_key_stock[0]["date"],
    "language": "en",
    "sortBy": "relevancy"
}


news_data = get_news_api_data()
add_top3_news_from_news_api()

yesterday_data = index_key_stock[0]
data_2_days_before = index_key_stock[1]

price_difference_yest_2days_before = (yesterday_data["price"] - data_2_days_before["price"])
percentage_difference = (price_difference_yest_2days_before / yesterday_data["price"]) * 100

## STEP 3: Use https://www.twilio.com

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

send_top3_news_to_mobile()


