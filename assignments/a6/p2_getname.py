import tweepy
from tweepy import *
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
CONSUMER_KEY = "YwekEH9UrlXUFKUH2XmImE681"
CONSUMER_SECRET = "NWaB0jN5HaQ3f9VqCrMhP2nP8154KGXoPeDxZk6TIOVptAxErb"

OAUTH_TOKEN = "4860544225-qbjIQvrGlrj493eIHAjNu2OH0rdrHlM94XMHe1x"
OAUTH_TOKEN_SECRET = "vfAc4sJwbWExBjrMZiMqRMuknTzbl2le55DKX5gGYOOXR"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api=tweepy.API(auth)

fdata=open('followers_name.txt','w')
user=api.get_user('joc7188')

fdata.write(user.name+'\n')

for user in tweepy.Cursor(api.followers, screen_name="joc7188",count=200).items():
	#users.append(user) 
	fdata.write(user.name+'\n')
fdata.close()