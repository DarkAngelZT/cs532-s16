import requests
import sys
from bs4 import BeautifulSoup

def get_rss(fname):
	page=open('rawBlogs/pages/'+fname)
	text=page.read()
	page.close()
	soup=BeautifulSoup(text)
	links=soup.find_all('link',{'type':'application/rss+xml'})
	if links:
		return str(links[0]['href'])
	return None

outfile=open('feeders.txt','w')
pathfile=open('rawBlogs/uriList')
paths=pathfile.readlines()
for line in paths:
	filename=line.split(' ')[0]
	uri=get_rss(filename)
	if uri :
		outfile.write(uri+'\n')
pathfile.close()
outfile.close()