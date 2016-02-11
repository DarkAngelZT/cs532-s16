import requests
import sys
def getRealUrl(url):
	try:
		r=requests.get(url)
		if r.status_code==200:
			return r.url
	except Exception, e:
		return None

rawFile=open("url_raw.txt")
lines=rawFile.readlines()
list_url=set()
print('loading raw data...')
for line in lines:
	url=getRealUrl(line)
	if url is not None:
		list_url.add(url)
		l=len(list_url)
		sys.stdout.write("\r"+str(l/10.0)+"%")
		sys.stdout.flush()
		if l >=1000:
			break
rawFile.close()
print('load finished, start writing file...')
newFile=open('url_list.txt','w')
for r_url in list_url:
	newFile.write(r_url+"\n")
newFile.close()
