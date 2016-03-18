import tweepy
from tweepy import *
import time
import os
CONSUMER_KEY = "YwekEH9UrlXUFKUH2XmImE681"
CONSUMER_SECRET = "NWaB0jN5HaQ3f9VqCrMhP2nP8154KGXoPeDxZk6TIOVptAxErb"

OAUTH_TOKEN = "4860544225-qbjIQvrGlrj493eIHAjNu2OH0rdrHlM94XMHe1x"
OAUTH_TOKEN_SECRET = "vfAc4sJwbWExBjrMZiMqRMuknTzbl2le55DKX5gGYOOXR"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api=tweepy.API(auth,wait_on_rate_limit =True, wait_on_rate_limit_notify=True)

fdata=open('followers.txt')
strlines=fdata.readlines()
usernames=list(line for line in strlines)
fdata.close()

outdata=open('net.txt','a')
for i in range(len(usernames)-1):
	for j in range(i+1,len(usernames)):
		while True:
			try:
				fs=api.show_friendship(source_screen_name = usernames[i],target_screen_name=usernames[j])
				index1=i
				index2=j
				sname1=fs[0].screen_name
				sname2=fs[1].screen_name
				linktype=3
				if fs[0].following or fs[0].followed_by :
					if fs[0].following :
						if fs[0].followed_by:
							linktype=2
						else:
							linktype=0
					else:
						if fs[0].followed_by:
							linktype=1
					if linktype!=3:
						outdata.write(str(i)+'\t'+str(j)+'\t'+sname1+'\t'+sname2+'\t'+str(linktype)+'\n')
				break
				#0: -->; 1: <--; 2: <-->
			except BaseException as e:
				print (str(e))
				if 'Not authorized' in str(e):
					break
				else:
					time.sleep(5)
					continue
			
		
		
outdata.close()
# fs=api.show_friendship(source_screen_name='joc7188',target_screen_name='ItsMyBell')
# print(fs[0])
# print(fs[1].following)