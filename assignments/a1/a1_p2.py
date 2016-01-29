#! /usr/bin/env python
import requests
import sys
from bs4 import BeautifulSoup

def getRealLocation(url):
	try:
		r=requests.get(url)
		if r.status_code==200:
			return url,r
		elif r.status_code>=300 and r.status_code<400:
			newUrl=r.headers['location']
			return digRealLocation(newUrl)
		else:
			return None,None
	except Exception as e:
		#print(e.message)
		return None,None

#script entry
if(len(sys.argv)!=2):
	print("Usage: a1_p2.py [url]")
	sys.exit(0);
url,_=getRealLocation(sys.argv[1])
if url is None:
	print("Invalid url")
	sys.exit(-1)

soup=BeautifulSoup(requests.get(url).text)
pdflinks=[]
for link in soup.find_all('a'):
	realUrl,response=getRealLocation(link.get('href'))
	if realUrl is not None:
		if response.headers['Content-Type']=='application/pdf' :
			pdflinks.append([realUrl,response.headers['Content-Length']])

if len(pdflinks)>0:
	for unit in pdflinks:
		print(unit[0])
		print"size: %s bytes"%(unit[1])
else:
	print('There\'s no pdf on this page')