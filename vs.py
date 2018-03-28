import time, urllib, json, datetime, sys
import tweepy

urlCE1 = "https://www.coinexchange.io/api/v1/getmarketsummary?market_id=748"
urlCE2 = "https://www.coinexchange.io/api/v1/getorderbook?market_id=748"
response1 = urllib.urlopen(urlCE1)
try:
    data1 = json.loads(response1.read())
except ValueError:
    print 'Decoding URL1 JSON has failed'
    sys.exit()
response2 = urllib.urlopen(urlCE2)
try:
    data2 = json.loads(response2.read())
except ValueError:
    print 'Decoding URL2 JSON has failed'
    sys.exit()
#print data
bid = data1['result']['BidPrice']
ask = data1['result']['AskPrice']
#bbtc = float(bid) * float(border)
#bbtc = round(bbtc,8)
ask = float(ask) * 100000000
bid = float(bid) * 100000000
ask = int(round(ask))
bid = int(round(bid))
print("\n{}".format(datetime.datetime.now()))
print('BidPrice: {} sat'.format(bid))
print('AskPrice: {} sat'.format(ask))
ind = 0
st0 = datetime.datetime(2020, 12, 31, 0, 0, 0)
bt0 = datetime.datetime(2020, 12, 31, 0, 0, 0)
bq0 = 0
for ind in range(50):
#    print("{}".format(data2['result']['SellOrders'][ind]))
#    for i in range(len(data2['result']['SellOrders'])):
#    print("{}".format(data2['result']['SellOrders'][ind]['OrderTime']))
    st1 = data2['result']['SellOrders'][ind]['OrderTime']
    sq1 = int(float(data2['result']['SellOrders'][ind]['Quantity']))
    st1 = datetime.datetime.strptime(str(st1), "%Y-%m-%d %H:%M:%S" )
    bt1 = data2['result']['BuyOrders'][ind]['OrderTime']
    bq1 = int(float(data2['result']['BuyOrders'][ind]['Quantity']))
    bt1 = datetime.datetime.strptime(str(bt1), "%Y-%m-%d %H:%M:%S" )
    if st1 < st0:
        st0 = st1
        sq0 = sq1
    if bt1 < bt0:
        bt0 = bt1
        bq0 = bq1
    ind = ind + 1
print("先頭OB売注文:{} {:,} NANJ".format(str(st0), sq0))
print("先頭OB買注文:{} {:,} NANJ".format(str(bt0), bq0))
#int( time.mktime( datetime.datetime.strptime( str(st0), "%Y-%m-%d %H:%M:%S" ).timetuple() ) )
#for st1 in data2['result']['SellOrders']['OrderTime']:
#	int( time.mktime( datetime.datetime.strptime( str(st1), "%Y-%m-%d %H:%M:%S" ).timetuple() ) )
#	if st1 >= st0: st0 = st1
#print("{}".format(datetime.fromtimestamp(st0)))
consumer_key        = 'vGWC2o5YCrw2GPjVZwKVvtY66'
consumer_secret     = '25c8gSC4IrhBTlK7EqRvaDi3INhHO5KoakkTwVSoCvOVpf7VnD'
access_token        = '978827522212233217-oZxyfjIpfnnlNlUUuC6NX5OX4qmXxXj'
access_token_secret = 'BElcQ6yKvleFYFAGq8ZBBgEIeDg7VankMid2GAQt3aonN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth)
api.update_status(status = "先頭OB売注文:{} {} sat {:,} NANJ\n先頭OB買注文:{} {} sat {:,} NANJ".format(str(st0), ask, sq0, str(bt0), bid, bq0))
