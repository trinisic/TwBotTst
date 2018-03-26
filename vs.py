import time, urllib, json
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import tweepy

#options = Options()
#with urllib.request.urlopen("https://www.coinexchange.io/api/v1/getmarketsummary?market_id=748") as urlce:
#    data = json.loads(url.read().decode())
#data = json.loads(response.read())

urlce = "https://www.coinexchange.io/api/v1/getmarketsummary?market_id=748"
response = urllib.urlopen(urlce)
data = json.loads(response.read())
print data

prinf('BidPrice:{}'.format(data['result']['BidPrice']))
prinf('AskPrice:{}'.format(data['result']['AskPrice']))

# Chromeのパス
#options.binary_location = '/app/.apt/usr/bin/google-chrome'
# ヘッドレス
#options.add_argument('--headless')
#driver = webdriver.Chrome(chrome_options=options)
#driver.get('https://www.coinexchange.io/market/NANJ/BTC#NANJCOIN')
#売り板
#ask = driver.find_element_by_class_name('market-summary-ask-price').text
#sorder = driver.find_element_by_class_name('buy-amount').text
#sbtc = float(ask) * float(sorder)
#sbtc = round(sbtc,8)
#買い板
#bid = driver.find_element_by_class_name('market-summary-bid-price').text
#border = driver.find_element_by_class_name('sell-amount').text

#bbtc = float(bid) * float(border)
#bbtc = round(bbtc,8)
#driver.quit()  # ブラウザーを終了する
ask = float(ask) * 100000000
bid = float(bid) * 100000000
ask = int(round(ask))
bid = int(round(bid))

#consumer_key        = 'UEb18HBscs2h9Mhpe6KmsCTbz'
#consumer_secret     = 'r2ByglOgZm326rHXfAAG4J1SiF9KoEraKzMGKAbZFcBIcvQDye'
#access_token        = '113384111-05QVgLnhO23Z3cSP7OqjrM8skjzgS96tTncTGecY'
#access_token_secret = 'if0egdApemMhw64LaLJ8Eh3AOdN5GayOeKFfCdxQitzhQ'

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth_handler=auth)
#url = 'https://goo.gl/aUT2E3'
#api.update_status(status = "NANJCOIN板の情報をお知らせするやで〜\n"+"売:" + str(ask) +"satoshi  " \n                    VS\n買:" + str(bid) + "satoshi やで！\n詳しくはCEをチェックや！ほな、また！\n#NANJCOIN\n" + url)
