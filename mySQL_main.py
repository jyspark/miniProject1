from getandread import gettweets
from mediaURLs import getmediaURLs
from getimage import getimage
from description import description
import os
import mysql.connector

mydb = mysql.connector.connect(user='root', password='', host='127.0.0.1', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS miniProject3")
mycursor.execute("use miniProject3")
mycursor.execute("CREATE TABLE IF NOT EXISTS user_data (id INT AUTO_INCREMENT PRIMARY KEY,Username VARCHAR(255), imgNum VARCHAR(255), description VARCHAR(255),description_num VARCHAR(255))")
mycursor.execute("use miniProject3")

tweethandle = input("Enter the Username: @")

mycursor.execute("SELECT * FROM user_data WHERE username='"+tweethandle+"'")
myresult = mycursor.fetchall()

print("*****Entering Get Tweet Stage*****")
initTweet = gettweets(tweethandle)
print("*****Entering Get MediaURLs Stage*****")
initMedia = getmediaURLs(initTweet)
print("*****Entering Get Image Stage*****")
imgNum = getimage(initMedia)
print("*****Entering Lable Stage*****")
description(tweethandle,imgNum)

print("\n\n\n")
ans = input("Do you want to print database? Yes=1,No=2")
if ans == 1:
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("There are ",len(myresult),"users in database")
    print("The current database is ")
    num=0
    desc=[]
    for user in myresult:
        num=num+int(user[2])
        curr_des=user[3].split(',')
        for j in curr_des:
            desc.append(j)
        print(user)
    if (len(myresult)>0):
        print("Some statistics:")
        print("The most popular description is",(max(set(desc), key = desc.count)))
        print("There is an average of",str(num/len(myresult)),"images per feed")

        ans = input("Do you want to search for a word? Yes=1,No=2")
        if ans == 1:
            word=input("Enter a word to search: ")
            mycursor.execute(("SELECT * FROM user_data"))
            myresult = mycursor.fetchall()
            print("The next user has the word",word,"in their description:")
            for user in myresult:
                desc=user[3]
                desc=desc.split(',')
                if word in desc:
                    print(user[1])
        else:
            exit()

else:
    exit()
