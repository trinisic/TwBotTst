import time, urllib, json
import tweepy

urlCE = "https://www.coinexchange.io/api/v1/getmarketsummary?market_id=748"
response = urllib.urlopen(urlCE)
data = json.loads(response.read())
#print data
bid = data['result']['BidPrice']
ask = data['result']['AskPrice']
#bbtc = float(bid) * float(border)
#bbtc = round(bbtc,8)
ask = float(ask) * 100000000
bid = float(bid) * 100000000
ask = int(round(ask))
bid = int(round(bid))
print('BidPrice: {} sat'.format(bid))
print('AskPrice: {} sat'.format(ask))
sot = max(data['SellOrders']['OrderTime'] for OrderTime in data)
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
