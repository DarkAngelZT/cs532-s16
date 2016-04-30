#!/usr/bin/python
import feedparser
import re

def get_pure_text(text):
  t=re.compile(r'<[^>]+>')
  return t.sub('',text)
# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(title,summary):
  wc={}

  # Extract a list of words
  words=getwords(title+' '+summary)
  for word in words:
    wc.setdefault(word.strip(),0)
    wc[word]+=1
  return title,wc

def getwords(html):
  # Remove all the HTML tags
  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  return [word.lower() for word in words if word!='']

#-------script entry--------
apcount={}
wordcounts={}
f=feedparser.parse('rawRSS.txt')
counter=0
for entry in f['entries']:
  title = get_pure_text(entry['title'].encode('utf-8'))
  summary = get_pure_text(entry['summary'].encode('utf-8'))

  title,wc=getwordcounts(title,summary)
  wordcounts[title]=wc
  for word,count in wc.items():
    apcount.setdefault(word,0)
    if count>1:
      apcount[word]+=1
  counter+=1
  if counter>=100:
    break

wordlist=[]
for w,bc in apcount.items():
  frac=float(bc)/100
  #if frac>0.01 and frac<0.5:
  wordlist.append(w)
  if len(wordlist)>=500 :
    break

out=file('feedData.txt','w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  #print blog
  try:
    out.write(blog)
  except:
    out.write(str(blog.encode('utf-8')))
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')