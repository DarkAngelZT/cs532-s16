import math
from math import *
import scipy
from scipy import stats
from scipy.spatial import distance
users={}
movies={}
linktable={}

correlation={}
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
#calculate correlation
pickedId='893'
pickedUser=linktable[pickedId]
for uid in linktable :
	if uid==pickedId:
		continue
	pickedUserRating=[]
	currentUserRating=[]
	for mid in pickedUser:
		if linktable[uid].has_key(mid) :
			pickedUserRating.append(pickedUser[mid])
			currentUserRating.append(linktable[uid][mid])
	if len(currentUserRating)==0 :
		correlation[uid]=0
	else:
		correlation[uid]=scipy.stats.pearsonr(pickedUserRating,currentUserRating)[0]
		if not correlation[uid] or math.isnan(correlation[uid]) :
			correlation[uid]=float(1)/(float(1)+scipy.spatial.distance.euclidean(pickedUserRating,currentUserRating))

correlationArray=sorted(correlation,key=correlation.get,reverse=True)
print('5 users are most correlated to the substitute you:')
for i in  range(5) :
	print(correlationArray[i]+'  ( correlation: '+str(correlation[correlationArray[i]])+' ) ')

print('5 users are least correlated to the substitute you:')
for j in range(-1,-6,-1):
	print(correlationArray[j]+' ( correlation: '+str(correlation[correlationArray[j]])+' ) ')