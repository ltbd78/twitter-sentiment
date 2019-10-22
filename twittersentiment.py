import tweepy
from textblob import TextBlob

consumer_key = 'q4IK11kpSi0s5Q5QWNiHIdmdJ'
consumer_secret = 'c63yKGaJ83y1Uuvf2AIbRx5ocMtu9sSGvbOsNcybFvVESUGgSN'
access_token = '211712377-B0zeFBgg1hphUEfVIi2UNk7lO3TpF4t8hJ8VrdaW'
access_token_secret = 'noIb2LbMgSI3RZOqdrNh36YCDNJIAqY4VggICu4xabTXz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        userid = status.id
        try:
            tweet = status.extended_tweet['full_text']
        except Exception as e:
            tweet = status.text 
        if 'RT @' not in tweet:
            tb = TextBlob(tweet)
            #print(api.get_user(userid).screen_name)
            #print(status.user.name)
            print(status.user.screen_name + ' | ' + str(round(tb.sentiment.polarity, 3)))
            print(tweet) 
            print('-'*60)
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

if __name__ == '__main__':
    query = input('Enter Search Query: ')
    print('\n')
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended')
    myStream.filter(track=[query])
