#coding: utf-8
import requests
from bs4 import BeautifulSoup
import tweepy

#スクレイピング
target_url = 'https://www.coinexchange.io/market/NANJ/BTC'
r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')

last = soup.find(class_='market-summary-last-price').string
vol = soup.find(class_='market-summary-volume').string
high = soup.find(class_='market-summary-high').string
low = soup.find(class_='market-summary-low').string
trade = soup.find(class_='market-summary-trade-count').string
last = float(last) * 100000000
high = float(high) * 100000000
low = float(low) * 100000000
last = int(round(last))
high = int(round(high))
low = int(round(low))

#呟き
consumer_key        = 'UEb18HBscs2h9Mhpe6KmsCTbz'
consumer_secret     = 'r2ByglOgZm326rHXfAAG4J1SiF9KoEraKzMGKAbZFcBIcvQDye'
access_token        = '113384111-05QVgLnhO23Z3cSP7OqjrM8skjzgS96tTncTGecY'
access_token_secret = 'if0egdApemMhw64LaLJ8Eh3AOdN5GayOeKFfCdxQitzhQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth)
url = 'https://goo.gl/aUT2E3'
api.update_status(status = "NANJCOINの価格をテスト\n現在の価格は" + str(last) + "satoshi\n24時間での最高金額は" + str(high) + "satoshi\n最低金額は" + str(low) + "satoshi\n取引額は" + vol + "btc\n取引回数は" + trade + "回\n)
