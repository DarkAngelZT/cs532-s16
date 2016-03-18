import datetime
gfile=open('gender.txt')
strline=gfile.readlines()
gender={}
nmale=0
nfemale=0
for line in strline:
	tuples=line.split('\t')
	if tuples[1].strip() == 'male':
		nmale=nmale+1
	else:
		nfemale=nfemale+1
	gender[tuples[0]]=tuples[1].strip()
gfile.close()

idfile=open('followers.txt')
namefile=open('followers_name.txt')
namedict={}
idlist=list(idfile.readlines())
namelist=list(namefile.readlines())
for i in range(len(idlist)):
	namedict[idlist[i].strip()]=namelist[i].strip()
idfile.close()
namefile.close()

resultFile=open('p2_gender homophily.txt','w')
resultFile.write('Generated in %s\n'%datetime.datetime.now())
resultFile.write('Author: Neo <Zetan Li>\n\n')
resultFile.write('Male : %d\n'%nmale)
resultFile.write('Female : %d\n'%nfemale)
p=float(nmale)/float(nmale+nfemale)
q=float(nfemale)/float(nmale+nfemale)
pq=2*p*q
resultFile.write('p = %.2f\nq = %.2f\n2pq = %.2f\n\n'%(p,q,pq))

resultFile.write('Cross gender links:\n')
resultFile.write('------------------------------------------------\n')
linkfile=open('net.txt')
strline=linkfile.readlines()
ncross=0
nlinks=0
for line in strline:
	tuples=line.split('\t')
	if namedict[tuples[2]] not in gender or namedict[tuples[3]] not in gender :
		continue
	gender1=gender[namedict[tuples[2]]]
	gender2=gender[namedict[tuples[3]]]
	if gender1 != gender2:
		ncross=ncross+1
		resultFile.write('%s <----> %s\n'%(namedict[tuples[2]],namedict[tuples[3]]))
	nlinks=nlinks+1
linkfile.close()
resultFile.write('\nSummary of cross gender links: %d out of %d\n'%(ncross,nlinks))
if nlinks>0:
	resultFile.write('Percentage of cross gender links : %.2f'%(float(ncross)/float(nlinks)))
resultFile.close()