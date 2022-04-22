import requests
from newsapi import NewsApiClient
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "WH5QK7OJ0TWX9OT9"
NEWS_API_KEY = "3dfd53b3e7404cd69f2beb54074ba436"
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":STOCK_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query",params=parameters)
result = response.json()["Time Series (Daily)"]#Get only daily data without metadata.
new_dict = {key:value["4. close"] for key,value in dict(result).items()}#create a new dict with only close price and date
counter = 0
new_dict2 ={}
#convert dictionary from date key into index key, for easier access.
for key,value in new_dict.items():
    new_dict2[counter] = {
        "date":key,
        "price":float(value)
    }
    counter+=1
yesterday_data = new_dict2[0]
data_2_days_before = new_dict2[1]
print(new_dict2)
difference_of_yesterday_and_2_days_ago = (yesterday_data["price"]-data_2_days_before["price"])
percentage_difference = (difference_of_yesterday_and_2_days_ago/yesterday_data["price"])*100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# Init
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
print(top_headlines)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

