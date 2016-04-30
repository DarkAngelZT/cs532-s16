#!/usr/bin/python
from numpredict import *
fmeasure='F-Measure'
wlblog='Web Science and Digital Libraries Research Group'
vectors={}
vectorfm=[]
vectorwb=[]
datafile=open('blogdata.txt')
strline=datafile.readlines()
header=True
for line in strline:
	if header:
		#skip header
		header=False
		continue
	tuples=line.strip().split('\t')
	if tuples[0] == fmeasure:
		for i in range(1,len(tuples)):
			vectorfm.append(float(tuples[i]))
	elif tuples[0]==wlblog:
		for i in range(1,len(tuples)):
			vectorwb.append(float(tuples[i]))
	else:
		vectors[tuples[0]]=[]
		for i in range(1,len(tuples)):
			vectors[tuples[0]].append(float(tuples[i]))
datafile.close()

nn=knnestimate(vectors.values(),vectorfm,distance=cosine)
print ('----K nearest neighbors of F-Measure------------')
for k in [1,2,5,10,20]:
	print('k = %d'%k)
	for j in range(k):
		print('%s\t%.6f'%(vectors.keys()[nn[j][1]],nn[j][0]))
	print('')

nn=knnestimate(vectors.values(),vectorwb,distance=cosine)
print ('----K nearest neighbors of Web Science and Digital Libraries Research Group------------')
for k in [1,2,5,10,20]:
	print('k = %d'%k)
	for j in range(k):
		print('%s\t%.6f'%(vectors.keys()[nn[j][1]],nn[j][0]))
	print('')