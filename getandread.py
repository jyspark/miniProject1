#!/usr/bin/env python
##2018 Julie Park

import tweepy #https://github.com/tweepy/tweepy
import socket
from urllib.request import urlopen, URLError
import tweetkey

##Twitter API credentials
#consumer_key = "Enter API Key"
#consumer_secret = "Enter API secret Key"
#access_key = "Enter Access Token"
#access_secret = "Enter Access Token secret"

def gettweets(userID):
    ##authorize twitter, initialize tweepy need to remove tweetkey to run with your own keys
    auth = tweepy.OAuthHandler(tweetkey.consumer_key, tweetkey.consumer_secret)
    auth.set_access_token(tweetkey.access_key, tweetkey.access_secret)
    api = tweepy.API(auth)

    try:
        user= api.get_user(userID)
    except:
        print("Not Correct Handle or Does not Exist.")
        gettweets(input("Enter Again: @"))

    initTweet = []

    newtweets = api.user_timeline(screen_name = userID,count=200)

    initTweet.extend(newtweets)

    oldest = initTweet[-1].id - 1

    while len(newtweets) > 1000:
        newtweets = api.user_timeline(screen_name = userID,count=200,max_id=oldest)

        initTweet.extend(newtweets)

        oldest = initTweet[-1].id - 1
        if(len(initTweet) > 0):
            break

        #print(initTweet)
    print("Got tweets.\n")
    print("getandread.py DONEEEEEEEE")

    return initTweet
