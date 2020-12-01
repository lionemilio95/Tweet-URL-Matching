from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas as pd
import re
from urllib.request import urlopen
from sklearn.feature_extraction.text import TfidfVectorizer

consumer_key = 'TZTfGuWA0rtiKYDE28YTyjwQc'
consumer_secret = 'CpfEUzWJZABt61LcjJp5wehwKCmMjiXfKOZjim2dDrgZrAwqzo'
access_token = '1321595447136317446-rJzEDf0jcM5fwxTsbQVneaNiH3G6YT'
access_token_secret = 'CAse6TrYsLTASgwcDIs1PnNltsqeL887nKoESq1rupdIC'

# Create authentication for accessing Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Need to filter more on text
text_query = "console OR PS5 OR online game OR Xbox OR esports OR PC game"
count = 30
# full_text = True,
# tweet_mode='extended'

tweets_df = pd.DataFrame(columns=["Date", "ID", "Text"])

# Creation of query method using parameters
tweets = tweepy.Cursor(api.search, q=text_query, lang="en", tweet_mode='extended').items(10000)

# Pulling information from tweets iterable object
for tweet in tweets:
    id = tweet.id
    date = tweet.created_at
    if(hasattr(tweet, 'retweeted_status')):
        text = tweet.retweeted_status.full_text
    else:
        text = tweet.full_text
    tweets_df = tweets_df.append({"Date": date, "ID": id, "Text": text}, ignore_index=True)

tweets_df.to_csv("Video_games.csv",encoding='utf-8-sig')