from getandread import gettweets
from mediaURLs import getmediaURLs
from getimage import getimage
from description import description
import pymongo


tweethandle = input("Enter the Username: @")

print("*****Entering Get Tweet Stage*****")
initTweet = gettweets(tweethandle)
print("*****Entering Get MediaURLs Stage*****")
initMedia = getmediaURLs(initTweet)
print("*****Entering Get Image Stage*****")
imgNum = getimage(initMedia)
print("*****Entering Lable Stage*****")
description(tweethandle,imgNum)

ans = input("Enter a username to search: ")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["users"]

if (mycol.count()==0):
    print("No such user name")
else:
    for user in mycol.find():
        if (user.get('username')==ans):
            print(user)
ans = input("Do you want to print database?Yes=1,No=2")

if ans == 1:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    print("There are ",mycol.count(),"users at data base")
    print("The current data base is :")
    num=0
    desc=[]
    for user in mycol.find():
        print(user)
        num=num+user.get('img_num')
        curr_des=user.get('description').split(',')
        for j in curr_des:
            desc.append(j)
    if (mycol.count()>0):
        print("Some statistics:")
        print("The most popular description is",(max(set(desc), key = desc.count)))
        print("There is an average of",str(num/mycol.count()),"images per feed")

    ans = input("Do you want to search for a word? Yes=1,No=2\n If you want to reset database press 3.")
    if ans == 1:
        word=input("What is the word?")
        print("The next user has the word",word,"in their description:")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        for user in mycol.find():
            desc=user.get('description')
            desc=desc.split(',')
            if word in desc:
                print(user.get('username'))
    elif ans == 3:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        x = mycol.delete_many({})
    else:
        exit()
else:
    exit()
