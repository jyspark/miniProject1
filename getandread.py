#!/usr/bin/env python
##Author: Julie P

import tweepy #https://github.com/tweepy/tweepy
import socket
from urllib.request import urlopen, URLError

##Twitter API credentials
#consumer_key = "Enter API Key"
#consumer_secret = "Enter API secret Key"
#access_key = "Enter Access Token"
#access_secret = "Enter Access Token secret"

#Twitter only allows access to a users most recent 3240 tweets with this method
def gettweets(userID):

    from mediaURLs import getmediaURLs   
   
    ##authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(tweetkey.consumer_key, tweetkey.consumer_secret)
    auth.set_access_token(tweetkey.access_key, tweetkey.access_secret)
    api = tweepy.API(auth)
    

    try:         #Run when the handle is existed 
        user= api.get_user(userID)

        ##initialize a list to hold all the tweepy Tweets
        initTweet = []    
    
        ##make initial request for most recent tweets (200 is the maximum allowed count)
        newtweets = api.user_timeline(screen_name = userID,count=200)

        ##save most recent tweets
        initTweet.extend(newtweets)
    
        ##save the id of the oldest tweet less one
        oldest = initTweet[-1].id - 1
    
        ##keep grabbing tweets until there are no tweets left to grab
        while len(newtweets) > 0:
        
            ##all subsiquent requests use the max_id param to prevent duplicates
            newtweets = api.user_timeline(screen_name = userID,count=200,max_id=oldest)
        
            ##save most recent tweets
            initTweet.extend(newtweets)
        
            ##update the id of the oldest tweet less one
            oldest = initTweet[-1].id - 1
            if(len(initTweet) > 15):
                break
              
        #print(initTweet)
        print("Got tweets.\n")

        ##Call function getmediaURLS to get medial_URLs
        getmediaURLs(initTweet)

    except Exception:
        tweethandle = input("Not correct Handle. \nEnter again: @")
        gettweets("@"+tweethandle)
    

##Check the availability of Twitter  
socket.setdefaulttimeout(20)
url = 'http://twitter.com/'

try:
    response = urlopen(url)
except URLError as e:
    print('We failed to reach a server. Reason:',str(e.code))
else: 
    ##Reads the handle and runs the program
    if __name__ == '__main__':
        #pass in the username of the account you want to download
        tweethandle = input("Enter the Username: @")
        gettweets("@"+tweethandle)


    

