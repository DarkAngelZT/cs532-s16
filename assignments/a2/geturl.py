from twitter import *
import sys

CONSUMER_KEY = "YwekEH9UrlXUFKUH2XmImE681"
CONSUMER_SECRET = "NWaB0jN5HaQ3f9VqCrMhP2nP8154KGXoPeDxZk6TIOVptAxErb"

OAUTH_TOKEN = "4860544225-qbjIQvrGlrj493eIHAjNu2OH0rdrHlM94XMHe1x"
OAUTH_TOKEN_SECRET = "vfAc4sJwbWExBjrMZiMqRMuknTzbl2le55DKX5gGYOOXR"

auth = OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
stream = TwitterStream(auth = auth, secure = True)

tweet_iter = stream.statuses.filter(track='game,sports,movie,comic,PUA,fitness')
url_counter=0
urlfile=open("url_raw.txt","w")
for tweet in tweet_iter:
	if url_counter>=10000:
		break;
	if "entities" in tweet:
		if "urls" in tweet["entities"]:
			for url in tweet["entities"]["urls"] :
				urlfile.write(url["expanded_url"]+"\n")
				url_counter=url_counter+1
				if url_counter>=10000:
					break
				sys.stdout.write("\r"+str(url_counter/100.00)+"%")
				sys.stdout.flush()
urlfile.close()