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
api=tweepy.API(auth)
users = []
fdata=open('twitter.data.raw','w')
user=api.get_user('phonedude_mln')
users.append({'count':user.followers_count,'name':'Michael L. Nelson'})

for user in tweepy.Cursor(api.followers, screen_name="phonedude_mln",count=200).items():
	#users.append(user) 
	users.append(dict({'name':user.screen_name,'count':user.followers_count}))
print("followers list got.")
#print("request follower count for each follower...")
# for u in users:
# 	try:
# 		fuser=api.get_user(u)
# 		users.append({u,fuser.followers_count})
# 	except Exception, e:
# 		print ('We got a timeout ... Sleeping for 15 minutes')
# 		time.sleep(15*60)
# 		fuser=api.get_user(u)
# 		users.append({u,fuser.followers_count})
        		
print("Finished, writing files...")	
for tu in users:
	fdata.write(str(tu['count'])+"\t"+tu['name']+'\n')
os.system('sort -n -k1 twitter.data.raw > twitter.data')
fdata.close()