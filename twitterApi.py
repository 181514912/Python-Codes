# retrieve a list of a user's friends and their statuses from twitter
import tweepy
import time
from tweepy import OAuthHandler

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except:
			time.sleep(60)

consumer_key='lHF68r2Es6tpSgTqeFiP94UsL'
consumer_secret='V3QbZrq3zddQPzea0ZOBi8woQTZO8R7zm5gtR33aHz7tCsNOQr'
access_token='796282115369242624-2Y5rQsafJ9FPp5vm5lCDJpfUa34dGXa'
access_secret='K4Q1KKEbOpCdfZF0PmSMBQYVRHFxx83R6Pjn1Mp9rZrEN'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)

count=0
for friend in limit_handled(tweepy.Cursor(api.friends).items()):
	count=count+1
	if count>7:break
	print friend.screen_name
	status=friend.status
	if status:
		txt=status.text
		print ' ',txt

print count
