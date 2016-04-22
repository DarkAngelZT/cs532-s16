import feedparser
import docclass
import re
def get_pure_text(text):
    t=re.compile(r'<[^>]+>')
    return t.sub('',text)
# Takes a filename of URL of a blog feed and classifies the entries
def read(feed,classifier):
  # Get feed entries and loop over them
  f=feedparser.parse(feed)
  counter=0
  result=[]
  for entry in f['entries']:
    title = get_pure_text(entry['title'].encode('utf-8'))
    summary = get_pure_text(entry['summary'].encode('utf-8'))

    print
    print '-----'
    print('#%d'%counter)
    # Print the contents of the entry
    print 'Title:     '+title
    print
    
    # Combine all the text to create one item for the classifier
    fulltext='%s\n%s' % (title,summary)
    currentFeed={}
    currentFeed['title']=title
    guess=str(classifier.classify(fulltext))
    currentFeed['guess']=guess
    print ('Guess: '+ guess)
    actual=raw_input('Enter Category: ')
    currentFeed['actual']=actual
    if counter<50:
        classifier.train(fulltext,actual)
    result.append(currentFeed)

    counter+=1
    if counter>=100:
        break
  return result

def calculateProb(table,classifier):
    for entry in table:
        entry['cprob']=classifier.cprob(entry['title'],entry['actual'])
        entry['fisherprob']=classifier.fisherprob(entry['title'],entry['actual'])
    return table

def WriteFile(data):
    table=open('p2_table.txt','w')
    for entry in data:
        table.write('%s\t%s\t%s\t%f\t%f\n'%(entry['title'],entry['guess'],entry['actual'],entry['cprob'],entry['fisherprob']))
    table.close()
#####script entry#########
fc=docclass.fisherclassifier(docclass.getwords)
fc.setdb("zlGames.db")
data=read('http://cdn.us.playstation.com/pscomauth/groups/public/documents/webasset/rss/playstation/Games_PS3.rss',fc)
table=calculateProb(data,fc)
WriteFile(table)