import time, urllib, json
import tweepy

urlCE1 = "https://www.coinexchange.io/api/v1/getmarketsummary?market_id=748"
urlCE2 = "https://www.coinexchange.io/api/v1/getorderbook?market_id=748"
response1 = urllib.urlopen(urlCE1)
data1 = json.loads(response1.read())
response2 = urllib.urlopen(urlCE2)
data2 = json.loads(response2.read())
#print data
bid = data1['result']['BidPrice']
ask = data1['result']['AskPrice']
#bbtc = float(bid) * float(border)
#bbtc = round(bbtc,8)
ask = float(ask) * 100000000
bid = float(bid) * 100000000
ask = int(round(ask))
bid = int(round(bid))
print('BidPrice: {} sat'.format(bid))
print('AskPrice: {} sat'.format(ask))

sot = max(data2['SellOrders']['OrderTime'] for OrderTime in data2)
print("{}".format(sot))
#consumer_key        = 'UEb18HBscs2h9Mhpe6KmsCTbz'
#consumer_secret     = 'r2ByglOgZm326rHXfAAG4J1SiF9KoEraKzMGKAbZFcBIcvQDye'
#access_token        = '113384111-05QVgLnhO23Z3cSP7OqjrM8skjzgS96tTncTGecY'
#access_token_secret = 'if0egdApemMhw64LaLJ8Eh3AOdN5GayOeKFfCdxQitzhQ'

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth_handler=auth)
#url = 'https://goo.gl/aUT2E3'
#api.update_status(status = "NANJCOIN - 売: {}sat 買: {}sat".format(ask, bid))
#最も直近に売買成立した買い注文、売り注文の注文時刻
