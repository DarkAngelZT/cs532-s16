tfile=open('p2_table.txt')
strlines=tfile.readlines()
category={
	'fighting':{'TP':0,'FP':0,'FN':0},
'sports':{'TP':0,'FP':0,'FN':0},
'rpg':{'TP':0,'FP':0,'FN':0},
'arpg':{'TP':0,'FP':0,'FN':0},
'racing':{'TP':0,'FP':0,'FN':0},
'platform':{'TP':0,'FP':0,'FN':0},
'action':{'TP':0,'FP':0,'FN':0},
'fps':{'TP':0,'FP':0,'FN':0}
}
for line in strlines:
	tuples=line.split('\t')
	title=tuples[0]
	guess=tuples[1]
	actual=tuples[2]
	if guess==actual:
		category[actual]['TP']+=1
	else:
		category[actual]['FN']+=1
		category[guess]['FP']+=1
tfile.close()

for c in category:

	category[c]['pre']=float(category[c]['TP'])/float(category[c]['TP']+category[c]['FP'])
	category[c]['recall']=float(category[c]['TP'])/float(category[c]['TP']+category[c]['FN'])
	if category[c]['pre']==0:
		category[c]['f']=0
	else:
		category[c]['f']=2*float(category[c]['pre'])*float(category[c]['recall'])/float(category[c]['pre']+category[c]['recall'])

outfile=open('p3_table.txt','w')
for cat in category:
	outfile.write('%s\t%d\t%d\t%d\n'%(cat,category[cat]['TP'],category[cat]['FP'],category[cat]['FN']))
outfile.close()

rfile=open('p3_performance.txt','w')
for cat in category:
	rfile.write('%s\t%f\t%f\t%f\n'%(cat,category[cat]['pre'],category[cat]['recall'],category[cat]['f']))
rfile.close()