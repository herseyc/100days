import requests
from datetime import datetime, timedelta, date

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

av_api_key = ""
news_api_key =""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": av_api_key
}


response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()['Time Series (Daily)']


data_list = [value for (key, value) in data.items()]

yesterdays_data = data_list[0]
yesterday_closing_price = yesterdays_data["4. close"]

daybefore_data = data_list[1]
daybefore_closing_price = daybefore_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(daybefore_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

print(diff_percent)

if diff_percent > 5:
    #print("Get news")

    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
        "sortBy": "publishedAt"
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    # slice to get first 3 articles
    news = news_response.json()['articles'][:3]
    #print(news)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    news_list = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in news]

#TODO 9. - Send each article as a separate message via Twilio. 
    for news_item in news_list:
       print(news_item)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

