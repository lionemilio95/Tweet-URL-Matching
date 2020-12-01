# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6_S8WFXabYiGQGyoPnQbH7-NLYYXEjU

## Twitter API
"""

from tweepy.streaming import StreamListener

from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas as pd
import re
from urllib.request import urlopen
from sklearn.feature_extraction.text import TfidfVectorizer

consumer_key = 'A4oTATSCjgyZGVukC3m0X3cVN'
consumer_secret = 'twVFqkkm8FJ17pFu44aph9TNGILmzBMazctbliwzdTcZRsDYnz'
access_token = '1321595401678462978-yJNmIQC55YykxsPDSpdsxSuMTyPNpq'
access_token_secret = 'VUz5CdC5Z0EwzQodKHQAHzLCupf66ZfOyxvVUcrVjrpfJ'

# Create authentication for accessing Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Need to filter more on text
text_query = "medicine OR health OR vaccine OR cough OR recovery OR fever OR stomach ache OR flu OR heal OR FDA"
# count = 30
# full_text = True,
# tweet_mode='extended'

tweets_df = pd.DataFrame(columns=["Date", "ID", "Text"])

# Creation of query method using parameters
tweets = tweepy.Cursor(api.search, q=text_query, lang="en", tweet_mode='extended').items(10000)

counter = 1
# Pulling information from tweets iterable object
for tweet in tweets:
    id = tweet.id
    date = tweet.created_at
    if hasattr(tweet, "retweeted_status"):
    	text = tweet.retweeted_status.full_text
    else:
    	text = tweet.full_text

    tweets_df = tweets_df.append({"Date": date, "ID": id, "Text": text}, ignore_index=True)

    counter = counter + 1

    if counter == 1000:
    	counter = 1
    	tweets_df = tweets_df.drop_duplicates()
    	tweets_df.to_csv("Meds.csv", mode='a', header=False)


#print(tweets_df["Text"][4])
tweets_df = tweets_df.drop_duplicates()
tweets_df.to_csv("Meds.csv", mode='a', header=False)