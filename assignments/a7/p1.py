users={}
movies={}
linktable={}
#parse rating file
linkfile=open('ml-100k/u.data')
strline=linkfile.readlines()
for line in strline:
	uid,itemid,rating,_=line.split('\t')
	if uid not in linktable:
		linktable[uid]={}
	linktable[uid][itemid]=int(rating)
linkfile.close()
#parse movie file
moviefile=open('ml-100k/u.item')
strline=moviefile.readlines()
for line in strline:
	tuples=line.split('|')
	movies[tuples[0]]=tuples[1]
moviefile.close()
#parse user file and filter
datafile=open('ml-100k/u.user')
strline=datafile.readlines()
for line in strline:
	tuples=line.split('|')
	if tuples[1] == '25' and  tuples[2]=='M' and tuples[3]=='student' :
		print (line.strip())
		movielist=sorted(linktable[tuples[0]],key=linktable[tuples[0]].get,reverse=True)
		for i in  range(3) :
			print(movies[movielist[i]]+'  --->  '+str(linktable[tuples[0]][movielist[i]])+' ;  '),
		print
		for j in range(-1,-4,-1):
			print(movies[movielist[j]]+'  --->  '+str(linktable[tuples[0]][movielist[j]])+' ;  '),
		print